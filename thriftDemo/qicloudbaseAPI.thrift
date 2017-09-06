/*
**************************************************************
        奇观云计算虚拟化技术基础平台 thrift 开发接口定义文件
                                        2017年7月26日
**************************************************************
*/

namespace java com.core
//异常信息
exception QiException
{
  1: i32 errorCode;
  2: string message;
}
//版本信息
struct QiVersionInfo
{
	1:string version ;
}

struct QiHostResInfo
{
	1:string model;
	2:i32 cpus;
	3:i32 mhz;
	4:i32 nodes;
	5:i32 sockets;
	6:i32 cores;
	7:i32 threads;
	8:i32 runningVMs ;
	9:i64 memory;
	10:i64 freememory;


}
struct  QiHostInfo
{
    1:i32 id ;
    2:string name ;
    3:string ip ;
    4:string clusterid ;
    5:string state ;
    6:string macaddr ;
    7:i32 maxvms ;
    8:string createtime ;
    9:string primaryPoolState ;//主存储状态
    10:string secondaryPoolState ;//辅助存储状态
    //11:virConnectPtr connectPtr ;//节点域
    11:QiHostResInfo resInfo ;
}
//模板信息
struct QiTemplateInfo
{
    1:string id ;
    2:string name ;
    3:string fatherid ;
    4:string type ;// IMG (primary),ISO  ,USERDATA(secondary)
    5:string OStype ;
    6:string OSversion ;
    7:string state ;
    8:string storageid ;
    9:string username ;
    10:i32 ispublic ;
    11:string createtime ;
} 
//存储信息
struct QiStorageInfo
{
    1:string id ;
    2:string name ;
    3:string type ;// primary , secondary
    4:string storageip ;
    5:i32 storagetype ;
    6:string sharepath ;
    7:string mountpath ;
    8:string state ;
    9:string createtime ;

    //i32 state;                     /* virStoragePoolState flags */
    10:i64 capacity;   /* Logical size bytes */
    11:i64 allocation; /* Current allocation bytes */
    12:i64 available;  /* Remaining free space bytes */

}
struct QiDiskInfo
{
    1:i32 id ;
    2:string instanceid ;
    3:string name ;
    4:i32 diskSize ;
    5:string diskMode;
    6:string createtime ;
}

struct QiInterfaceInfo
{
    1:i32 id ;
    2:string instanceid ;
    3:string type ;//接口类型，桥接， net,直接
    4:string mac ; //mac地址
    5:string mode ;//网卡类型 e1000， virtio
    6:string ip ;
    7:string createtime ;
}

struct QiInstanceBaseInfo
{
    1:string  id ;//uuid
    2:string  name ;//名称
    3:string  imgid ;//模板id
    4:string  isoid ;//iso文件id
    5:string  cpuType ;//cpu类型（core2duo  ,host）
    6:i16 cpuCores ;//cpu核心数
    7:i16 cpuThreads;//cpu线程数
    8:i16 cpuSockets ;//cpu插槽数
    9:i32 memorySize ;//内存大小（单位 MB）
    10:i32 diskSize ;//磁盘大小
    11:i16 diskMode;//磁盘类型 （ide，virtio）
    12:i16 displayProcotol ;//选择显示协议（vnc，spice ...）
    13:string createtime ;

    14:list<QiDiskInfo> diskInfo ;
    15:list<QiInterfaceInfo> i32erfaceInfo ;

}

struct QiInstanceInfo
{
    //节点信息
    1:QiHostInfo hostInfo ;
    2:QiInstanceBaseInfo baseInfo ;
    3:i32 procotol ;
    4:i32 state ;//状态信息（qiInstanceState ,QI_INSTANCES_RUNNING）
    5:i32 port1 ;
    6:i32 port2 ;
    7:string passwd ;//连接密码
    //virDomain *domain ;
}
service QicloudBaseApiServer
{
	//ping 测试接口
	string Ping(1:string str);
	//获取版本信息
	QiVersionInfo GetVersionInfo() ;
	//存储管理
	//添加存储
	i32 addStorageInfo(1:QiStorageInfo info) ;
	//删除存储
	i32 delStorageInfo(1:string id) ;
	//获取存储信息列表
	list<QiStorageInfo> getStorageInfoList() ;
	//模板管理
	//模板信息列表
	list<QiTemplateInfo> getTempalteInfoList();
	//添加模板
	i32 addTemplateInfo(1:QiTemplateInfo info);
	//删除模板
	i32 delTemplateInfo(1:string id) ;
	//修改模板信息
	i32 modifyTemplateInfo(1:QiTemplateInfo info) ;
	//获取指定模板信息
	QiTemplateInfo getTemplateInfo(1:string id) ;

	//集群管理
	//添加节点
	i32 addHostInfo(1:QiHostInfo info) ;
	//获取节点信息列表
	list<QiHostInfo> getHostInfoList() ;
	//删除节点
	i32 delHostInfo(1:string ip) ;
	//修改节点信息
	i32 modifyHostInfo(1:QiHostInfo info) ;
	//获取指定节点信息
	QiHostInfo getHostInfo(1:string ip ) ;
	//虚拟机操作

	//虚拟机管理
	//创建虚拟机(选择模板/iso)
	i32 createInstance(1:QiInstanceBaseInfo info) ;
	//启动虚拟机， 选择负载均衡策略 ， 选择启动的协议（vnc，spice，novnc，ssh ...）
	i32 startInstance(1:QiHostInfo info ,2:string uuid , 3:i32 displayProcotol);
	//添加网卡
	i32 addinterfaceInfo(1:string uuid ,2:QiInterfaceInfo info) ;
	//移除网卡
	i32 delinterfaceInfo(1:string uuid ,2:string id );
	//添加磁盘
	i32 addDiskInfo(1:string uuid ,2:QiDiskInfo info) ;
	//移除磁盘
	i32 delDiskInfo(1:string uuid ,2:string id) ;
	//添加iso文件
	i32 instanceAddISOFile(1:string uuid ,2:string isoid) ;
	//移除iso文件
	i32 instanceRemoveISOFile(1:string uuid ) ;
	//关机/重启/断电/重置
	i32 shutdownInstance(1:string uuid) ;
	i32 poweroffInstance(1:string uuid)  ;
	i32 resetInstance(1:string uuid) ;

        //删除虚拟机
        i32 delInstance(1:string id ) ;
        //获取虚拟机信息
        QiInstanceInfo getInstanceInfo(1:string uuid ) ;
        list<QiInstanceInfo> getAllInstanceInfoList() ;
}
