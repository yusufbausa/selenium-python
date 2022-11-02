from selenium.webdriver.common.by import By

class newCust():

    username = 'txtUsername'
    pwd = 'txtPassword'
    btn_login = 'lbLogin'
    role_marketing = '//*[@id="uModDRole_ctl00_gvRoles_lbSelectRole_1"]'

    btn_menu = 'imgMenu'
    btn_menu_customer = 'rModuleList_lbModuleList_1'
    btn_cust = '//*[@id="rtvMenuTree"]/ul/li[1]/div/a'

    btn_add_per_cust = 'lb_Toolbar_AddPersonal'
    field_cust_name = 'txtCustName'
    select_id_type = 'ucId_ucRefCustIdType_ddlReference'
    field_id_number = 'ucId_txtCustIdNo'
    field_id_expired = 'ucIdExpiredDt_txtDatePicker'
    field_birth_place = 'txtBirthPlace'
    field_birth_date = 'ucBirthDate_txtDatePicker'
    field_npwp = 'txtNpwp'
    field_mother_name = 'txtMotherMaidenName'

