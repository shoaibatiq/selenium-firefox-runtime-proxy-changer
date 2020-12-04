from selenium import webdriver
def mozilla_change_proxy(browser,proxy):
    
    
    print("Changing to :" + proxy)
    browser.get("about:config")
    
    browser.find_element_by_id("warningButton").click()
    proxy, port = str(proxy).split(":")
    setup_script = (
            'var prefs = Components.classes["@mozilla.org/preferences-service;1"].getService(Compone'
            'nts.interfaces.nsIPrefBranch);prefs.setIntPref("network.proxy.type", 1);'
            'prefs.setCharPref("network.proxy.http", "' + proxy + '");prefs.setIntPref("network.proxy.http_port", "'
            + port + '");prefs.setCharPref("network.proxy.ssl", "' + proxy + '");prefs.setIntPref'
            '("network.proxy.ssl_port", "' + port + '");prefs.setCharPref("network.proxy.ftp", "' + proxy + '");'
            'prefs.setIntPref("network.proxy.ftp_port", "' + port + '");')
    browser.execute_script(setup_script)
