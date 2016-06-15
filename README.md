This image use for CCDE Vmware VDI reset stauts analysis

Installation:
1) You can build the image by the Dockerfile

docker build -t="lennyleng/ccde_vdi_reset" .

2) You can pull the image from the alauda

docker pull index.alauda.cn/lennyleng/ccde_vdi_reset

Startup:
docker run -d -p 80:80 -e "DB_HOST=10.132.4.138" -e "DB_LOGIN_NAME=cloud\wx-xg018" -e "DB_LOGIN_PASS=123456" -e "DB_NAME=Event-DB" --name "ccde_vdi_reset" index.alauda.cn/lennyleng/ccde_vdi_reset

Usage:
http://yourip/?begin_time=2016-05-01&end_time=2016-06-01