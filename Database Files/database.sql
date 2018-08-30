create table pyscript.ticketInfo
(
	ticketID int not null comment '工单编号'
		primary key,
	platform varchar(255) null comment '业务平台',
	module varchar(255) null comment '业务模块',
	userType varchar(255) null comment '用户类型',
	companyName varchar(255) null comment '用户单位（公司）名称',
	mobile varchar(255) null comment '用户手机号码',
	qq varchar(255) null comment '用户QQ',
	district varchar(255) null comment '行政区划',
	category varchar(255) null comment '运维问题分类',
	specCategory varchar(255) null comment '具体问题分类（疑难、常规需要选择）',
	label varchar(255) null comment '处理标签',
	submitted varchar(255) null comment '提交人',
	submitTime datetime null comment '提交时间',
	brief longtext null comment '摘要',
	nowNode varchar(255) null comment '当前节点',
	nowStatus varchar(255) null comment '当前状态',
	processed varchar(255) null comment '当前处理人',
	finishTime datetime null comment '完结/废除时间',
	returned varchar(255) null comment '是否有回退',
	auditNode varchar(255) null comment '审核节点',
	customInfo longtext null comment '自定义项'
)
comment '工单基本信息'
;

create table pyscript.ticketProcess
(
	uuid varchar(255) not null comment '主键'
		primary key,
	auditNode varchar(255) null comment '审核节点',
	auditTime datetime null comment '审核时间',
	processor varchar(255) null comment '处理人',
	operation varchar(255) null comment '操作',
	commen longtext null comment '意见',
	customProce longtext null comment '自定义项',
	fs_id varchar(255) null comment '对应的工票id',
	constraint ticketProcess_uuid_uindex
		unique (uuid)
)
;

