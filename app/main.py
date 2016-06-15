#!flask/bin/python

import pymssql
import re
import json
import os

from flask import Flask,request
app = Flask(__name__)

@app.route('/')
@app.route('/get_ccde_vdi_reset')
def get_ccde_vdi_reset():
    begin_time = request.args.get('begin_time')
    end_time = request.args.get('end_time')
    if(begin_time == '' or begin_time == None or end_time == '' or end_time == None):
        return json.dumps({'ret_code' : 0, 'ret_data' : 'get method param not ok!'})
    
    try:
        conn = pymssql.connect(os.getenv('DB_HOST'), os.getenv('DB_LOGIN_NAME'), os.getenv('DB_LOGIN_PASS'), os.getenv('DB_NAME'))
        cursor = conn.cursor(as_dict=True)
    
        cursor.execute("select [Node], count(*) AS [Count], stuff( (select ',' + convert(varchar(128), [Time], 20) from [event] where [Node] = [event_tmp].[Node] and [EventType] = 'AGENT_STARTUP' and Time >= '%s' and [Time] <='%s' for xml path('') ), 1, 1, '' ) as [TimeSet] from [event] as [event_tmp] where [EventType] = 'AGENT_STARTUP' and Time >= '%s' and [Time] <='%s' group by [Node] order by [Count] DESC" % (begin_time, end_time, begin_time, end_time))
        ret_set = {'ret_code' : 1, 'ret_data' : []}
        
        for row in cursor:
            try:
                vdi_login_name = re.findall("^A-.+[^.cloud.ccde.cnpc]", row['Node'])[0][2:]
            except Exception,e:
                continue
        
            ret_set['ret_data'].append({'login_name' : vdi_login_name, 'reset_count' : row['Count'], 'reset_time' : row['TimeSet'].split(',')})
        
        conn.close()
        
    except Exception,e:
        return json.dumps({'ret_code' : 0, 'ret_data' : str(e)})
    
    return json.dumps(ret_set)
