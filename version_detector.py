def detect_version(banner):
    if banner is None:
        return {
            "software":None,
            "version": None
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