*** Settings ***
Library           LBMTest

*** Test Cases ***
connect
    ${server}    Set variable    {'servername':'KCBP00','protocol':0,'address':'10.1.93.106','port':21000, 'sendq':'req_rzrq','recvq':'ans_rzrq','username':'KCXP00', 'password':'888888'}
    log    ${server}
    ${lbmid}    Set variable    410502
    ${fixpram}    Set variable    funcid:410502,custid:240487053609,custorgid:2404,trdpwd:,netaddr:192.168.60.172,orgid:2404,operway:8,ext:0,custcert:,netaddr2:,
    ${unfixparam}    Set variable    fundid:240487053609,moneytype:0,remark:,
    ${sync_flag}    Set variable    1
    LBM Call True    ${server}    ${lbmid}    ${fixpram}    ${unfixparam}    ${sync_flag}
    LBM Call Ret Data    ${server}    ${lbmid}    ${fixpram}    ${unfixparam}

test
    ${test}    Set variable    helloworld
    log    ${test}

中文用例
    log    中文
