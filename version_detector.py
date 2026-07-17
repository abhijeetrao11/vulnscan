import re
def detect_version(banner):
    if banner is None:
        return {
            "software":None,
            "version": None
        }
    
    # -- ssh banner detection -- 
    
    if "OpenSSH" in banner:
        match = re.search(
            r"OpenSSH[_/]([\w\.\-p]+)", 
            banner
        )

        if match:
            return {
                "software":"OpenSSH",
                "version": match.group(1)
            }
        
    # -- ftp detection --
    if "vsFTPd" in banner:
        match = re.search(
            r"vsFTPd\s+([\d\.]+)",
            banner
        )

        if match:
            return {
                "software":"vsFTPd",
                "version": match.group(1)
            }
        
    
    if "Postfix" in banner:

        match = re.search(
            r"Postfix(?:\s*\((.*?)\))?",
            banner
        )

        version = None

        if match:
            version = match.group(1)
        

        return{
            "software":"Postfix",
            "version": version            
        } 
    
    if "Dovecot" in banner:
        return{
            "software":"Dovecot",
            "version": None            
        } 
    
    if "redis_version" in banner:
        match = re.search(
            r"redis_version:([\d\.]+)",
            banner
        )
        if match:
            return{
                "software":"Redis",
                "version":match.group(1)
            }
        return {
            "software":"Redis",
            "version":None
        }
        
    #-- my sql detection --
    if "mariadb" in banner.lower():

        match = re.search(
            r"(\d+\.\d+\.\d+)-MariaDB",
            banner,
            re.IGNORECASE
        )

        if match:
            return{
                "software":"MariaDB",
                "version":match.group(1)
            }
        

    
    if "postgresql" in banner.lower():
       
        
        match = re.search(r"PostgreSQL[\s/]([\d\.]+)", banner, re.IGNORECASE)
        
        if match:
            return{
                "software": "PostgreSQL",
                "version": match.group(1)
            }
        
        return{
            "software" : "PostgreSQL",
            "version": None
        }

    
    if "mysql" in banner.lower():
        match = re.search(
            r"(\d+\.\d+\.\d+)",
            banner
        )

        if match:
            return{
                "software":"MySQL",
                "version":match.group(1)
            }
        
    
     
    
    try:
        first_part = banner.split()[0]

        software , version = first_part.split("/",1)

        return {
            "software":software,
            "version":version
        }
    except Exception:
        return{
            "software": None,
            "version":None
        }