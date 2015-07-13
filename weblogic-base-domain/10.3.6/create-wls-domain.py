# Default domain 'base_domain' to be created inside the Docker image for WLS
# ==============================================

# WLS Configuration (will get preferably from env)
# -------------------------------
admin_port = int(os.environ.get("ADMIN_PORT", "7001"))
admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome01")

# Open default domain template
# ======================
readTemplate("/u01/oracle/weblogic/wlserver_10.3/common/templates/domains/wls.jar")

# Configure the Administration Server and SSL port.
# =========================================================
cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', admin_port)
set('LoginTimeoutMillis', 30000)

# Define the user password for weblogic
# =====================================
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_pass)

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode','prod')

domain_path = '/u01/oracle/weblogic/user_projects/domains/base_domain'

writeDomain(domain_path)
closeTemplate()

# Exit WLST
# =========
exit()
