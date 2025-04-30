import datetime
import json

from flask import Blueprint, request, render_template, redirect
from app import db
from app.models.opincome import OPIncome
from app.models.pa_op_registration import PA_OP_Registration
from app.models.ejksdzb import Ejksdzb
from sqlalchemy import and_, or_
from sqlalchemy.sql import func


outpmoney = Blueprint('outpmoney', __name__)

@outpmoney.route('/prod-api/api/CenterBugyingDrug/outpmoney', methods=['GET'])
def do():
    ret = []

    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    page = request.args.get('page')
    pagesize = request.args.get('pagesize')

    if startDate is None or startDate == '' or endDate is None or endDate == '':
        endDate = datetime.today().date()
        startDate = endDate.replace(day=1)
   
    if page is None or page == '':
        page = 1
    if pagesize is None or pagesize == 0:
        pagesize = 10


    # jdmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnameleve1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('jd_all_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname=='军队医改').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnameleve1, OPIncome.statisticsdate).all()
        
    # jdmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('jd_all_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname=='军队医改').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)

    
    # jddrugmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('jd_drug_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname=='军队医改',
    #     OPIncome.chargecategorycode.in_('A', 'M')).group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)

    # jdjcmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('jd_jc_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname=='军队医改',
    #     OPIncome.chargecategorycode=='C').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)

    # jdjymoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('jd_jy_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname=='军队医改',
    #     OPIncome.chargecategorycode=='D').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)
    
    # jd = jdmoney.union_all(jddrugmoney).union_all(jdjcmoney).union_all(jdjymoney).all()

    
    # dfmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('yb_all_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname!='军队医改').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)
    
    # dfdrugmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('yb_drug_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname!='军队医改',
    #     OPIncome.chargecategorycode.in_('A', 'M')).group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)

    # dfjcmoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('yb_jc_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname!='军队医改',
    #     OPIncome.chargecategorycode=='C').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)

    # dfjymoney = db.session.query(
    #     OPIncome.hospitalname, 
    #     OPIncome.deptnamelevel1, 
    #     OPIncome.statisticsdate,
    #     func.sum(OPIncome.totalmoney).label('yb_jy_money')).filter(
    #     OPIncome.statisticsdate>=startDate, 
    #     OPIncome.statisticsdate<=endDate,
    #     OPIncome.ybname!='军队医改',
    #     OPIncome.chargecategorycode=='D').group_by(
    #         OPIncome.hospitalname, OPIncome.deptnamelevel1, OPIncome.statisticsdate)


    # df = dfmoney.union_all(dfdrugmoney).union_all(dfjcmoney).union_all(dfjymoney).all()

    # result = jd.union_all(df).all()


    # jdfm = db.session.query(PA_OP_Registration, Ejksdzb).outerjoin(Ejksdzb, PA_OP_Registration.regdeptcode == Ejksdzb.deptcodelevel2).filter(
    #     PA_OP_Registration.isdeleted == 0, 
    #     PA_OP_Registration.returnregdata.is_(None),
    #     PA_OP_Registration.resourcetablekeyvalue.notlike('0%'),
    #     PA_OP_Registration.str3.notlike('%应检%'),
    #     PA_OP_Registration.str3.notlike('%尽检%')，
    #     PA_OP_Registration.str3.notlike('%冠状%')，
    #     PA_OP_Registration.str3.notlike('%新冠%')，
    #     PA_OP_Registration.regdate >= startDate,
    #     PA_OP_Registration.regdate <= endDate,
    #     PA_OP_Registration.ybname=='军队医改').group_by(
    #         PA_OP_Registration.visitnumber, 
    #         PA_OP_Registration.regdate, 
    #         Ejksdzb.deptcodelevel1,
    #         Ejksdzb.deptnamelevel1,
    #         PA_OP_Registration.str4,
    #         cardkindname)


    # ybfm = db.session.query(PA_OP_Registration, Ejksdzb).outerjoin(Ejksdzb, PA_OP_Registration.regdeptcode == Ejksdzb.deptcodelevel2).filter(
    #     PA_OP_Registration.isdeleted == 0, 
    #     PA_OP_Registration.returnregdata.is_(None),
    #     PA_OP_Registration.resourcetablekeyvalue.notlike('0%'),
    #     PA_OP_Registration.str3.notlike('%应检%'),
    #     PA_OP_Registration.str3.notlike('%尽检%')，
    #     PA_OP_Registration.str3.notlike('%冠状%')，
    #     PA_OP_Registration.str3.notlike('%新冠%')，
    #     PA_OP_Registration.regdate >= startDate,
    #     PA_OP_Registration.regdate <= endDate,
    #     PA_OP_Registration.ybname!='军队医改').group_by(
    #         PA_OP_Registration.visitnumber, 
    #         PA_OP_Registration.regdate, 
    #         Ejksdzb.deptcodelevel1,
    #         Ejksdzb.deptnamelevel1,
    #         PA_OP_Registration.str4,
    #         cardkindname)


    sql_op = '''select coalesce(ks,'其他') ks,
coalesce(sum(jdfm),0) as jdfm,
cast ( round(CASE WHEN coalesce(sum(jdfm),0)=0 THEN 0 ELSE SUM(jd_all_money)/SUM(jdfm) end 
 ,2)  as character varying ) as jd_all_jg,
 cast ( round(CASE WHEN coalesce(sum(jdfm),0)=0 THEN 0 ELSE SUM(jd_drug_money)/SUM(jdfm) end 
 ,2)  as character varying ) as jd_drug_jg,
  cast ( round(CASE WHEN coalesce(sum(jdfm),0)=0 THEN 0 ELSE SUM(jd_jc_money)/SUM(jdfm) end 
 ,2)  as character varying ) as jd_jc_jg,
  cast ( round(CASE WHEN coalesce(sum(jdfm),0)=0 THEN 0 ELSE SUM(jd_jy_money)/SUM(jdfm) end 
 ,2)  as character varying ) as jd_jy_jg,
 coalesce(sum(ybfm),0) as ybfm,
cast ( round(CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_all_money)/SUM(ybfm) end 
 ,2)  as character varying ) as yb_all_jg,
 cast ( round(CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_drug_money)/SUM(ybfm) end 
 ,2)  as character varying ) as yb_drug_jg,
  cast ( round(CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_jc_money)/SUM(ybfm) end 
 ,2)  as character varying ) as yb_jc_jg,
  cast ( round(CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_jy_money)/SUM(ybfm) end 
 ,2)  as character varying ) as yb_jy_jg,
 case when CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_all_money)/SUM(ybfm) end = 0 then 0 else CASE WHEN coalesce(sum(jdfm),0)=0 THEN 0 ELSE SUM(jd_all_money)/SUM(jdfm) end/CASE WHEN coalesce(sum(ybfm),0)=0 THEN 0 ELSE SUM(yb_all_money)/SUM(ybfm) end end jdb,
 count(*) OVER() as row_num
 from
(select hospitalname ,一级科室名称 as ks,date,
0 as jd_all_money,0 as jd_drug_money,0 as jd_jc_money,0 as jd_jy_money,
0 as yb_all_money,0 as yb_drug_money,0 as yb_jc_money,0 as yb_jy_money,
case when ybname in ('军队医改') then count(distinct visitnumber) end as jdfm,
case when ybname not in ('军队医改') then count(distinct visitnumber) end as ybfm
from
(
select 	  
case when reg.str4 = '10' then '玄武' when reg.str4 = '26' then '秦淮' else '其他' end as hospitalname,
dzb.一级科室代码,dzb.一级科室名称,reg.visitnumber,date(reg.regdate),cardkindname as ybname
from public.pa_op_registration  reg
left join  kb_datamining.ejksdzb dzb on  reg.regdeptcode=dzb.二级科室代码 and reg.regdeptname=dzb.二级科室名称
where reg.isdeleted='0'
and reg.regdate >='2021-06-10'
AND coalesce(reg.visitflaname,'其他') <> '退号'
AND reg.resourcetablekeyvalue not like '0%'
AND reg.returnregdate IS null
and (reg.str3 not like '%核酸%' and reg.str3 not like '%应检%' 
  and reg.str3 not like '%尽检%' and reg.str3 not like '%冠状%' 
  and reg.str3 not like '%新冠%')
and date(reg.regdate) >=cast('2025-04-01'  as timestamp)
and date(reg.regdate)<cast('2025-04-25' as timestamp)
group by reg.visitnumber,date(reg.regdate),dzb.一级科室代码,dzb.一级科室名称,reg.str4,cardkindname
) a
group by 一级科室名称,date,hospitalname,ybname
union all 
select hospitalname,deptnameleve1 as ks,statisticsdate as date,
sum(case when ybname in ('军队医改') then totalmoney end) as jd_all_money,
sum(case when chargecategorycode in ('A','M') and ybname in ('军队医改') then totalmoney else 0 end) jd_drug_money,
sum(case when chargecategorycode in ('C') and ybname in ('军队医改') then totalmoney else 0 end) jd_jc_money,
sum(case when chargecategorycode in ('D') and ybname in ('军队医改') then totalmoney else 0 end) jd_jy_money,
sum(case when ybname not in ('军队医改') then totalmoney end) as yb_all_money,
sum(case when chargecategorycode in ('A','M') and ybname not in ('军队医改') then totalmoney else 0 end) yb_drug_money,
sum(case when chargecategorycode in ('C') and ybname not in ('军队医改') then totalmoney else 0 end) yb_jc_money,
sum(case when chargecategorycode in ('D') and ybname not in ('军队医改') then totalmoney else 0 end) yb_jy_money,
0 as jdfm,0 as ybfm
from  kb_datamining.opincome  
where 1=1
and date(StatisticsDate) >=cast('2025-04-01'  as timestamp)
and date(StatisticsDate)<cast('2025-04-25' as timestamp)
group by hospitalname,deptnameleve1,statisticsdate
) a group by a.hospitalname,ks
order by ybfm'''
    # db.execute(sql_op)

    query = db.session.query(
        OPIncome.deptnameleve1, 
        func.sum(OPIncome.totalmoney).label('all_money'))
    jdmoney = query.filter(
        func.date(OPIncome.statisticsdate)>=startDate, 
        func.date(OPIncome.statisticsdate)<=endDate,
        OPIncome.ybname =='军队医改').group_by(OPIncome.hospitalno, OPIncome.deptnameleve1).all()
    jddrugmoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname == '军队医改',
        OPIncome.chargecategorycode.in_(['A', 'M'])).group_by(OPIncome.hospitalno, OPIncome.deptnameleve1).all()
    jdjcmoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname == '军队医改',
        OPIncome.chargecategorycode=='C').group_by(OPIncome.hospitalno, OPIncome.deptnameleve1).all()
    jdjymoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname == '军队医改',
        OPIncome.chargecategorycode == 'D').group_by(OPIncome.hospitalno, OPIncome.deptnameleve1).all()

    # jd = jdmoney.union_all(jddrugmoney).union_all(jdjcmoney).union_all(jdjymoney).all()
   
    dfmoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname!='军队医改').group_by(OPIncome.hospitalname, OPIncome.deptnameleve1).all()
    dfdrugmoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname!='军队医改',
        OPIncome.chargecategorycode.in_(['A', 'M'])).group_by(
            OPIncome.hospitalname, OPIncome.deptnameleve1).all()
    dfjcmoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname!='军队医改',
        OPIncome.chargecategorycode == 'C').group_by(
            OPIncome.hospitalname, OPIncome.deptnameleve1).all()
    dfjymoney = query.filter(
        func.date(OPIncome.statisticsdate) >= startDate, 
        func.date(OPIncome.statisticsdate) <= endDate,
        OPIncome.ybname != '军队医改',
        OPIncome.chargecategorycode == 'D').group_by(
            OPIncome.hospitalname, OPIncome.deptnameleve1).all()

    # df = dfmoney.union_all(dfdrugmoney).union_all(dfjcmoney).union_all(dfjymoney).all()
    # result = jd.union_all(df).all()

    for item in jdmoney:
        one = {}
        if item[0] is None or item[0] == '':
            continue
        one['ks'] = item[0]
        one['jd_all_jg'] = item[1]
        for i in jddrugmoney:
            if i[0] == item[0]:
                one['jd_drug_jg'] = i[1]
                continue
        for j in jdjcmoney:
            if j[0] == item[0]:
                one['jd_jc_jg'] = j[1]
                continue
        for k in jdjymoney:
            if k[0] == item[0]:
                one['jd_jy_jg'] = k[1]
                continue
        for l in dfmoney:
            if l[0] == item[0]:
                one['yb_all_jg'] = l[1]
                continue
        for m in dfdrugmoney:
            if m[0] == item[0]:
                one['yb_drug_jg'] = m[1]
                continue
        for n in dfjcmoney:
            if n[0] == item[0]:
                one['yb_jc_jg'] = n[1]
                continue
        for o in dfjymoney:
            if o[0] == item[0]:
                one['yb_jy_jg'] = o[1]
                continue
        ret.append(one)
    print(ret)








    return render_template('base.html')


    

