from version_detector import detect_version

print(
    detect_version(
        "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1"
    )
)

print(
    detect_version(
        "220 (vsFTPd 3.0.5)"
    )
)

print(
    detect_version(
        "redis_version:6.2.5"
    )
)

print(
    detect_version(
        "5.5.5-10.5.12-MariaDB"
    )
)

print(
    detect_version(
        "mysql 8.0.36"
    )
)

print(
    detect_version(
        "PostgreSQL 16.2"
    )
)