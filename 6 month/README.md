# 6-Month Track

A comprehensive track emphasizing Unix proficiency, Python development, and security operations.

## Structure

- Semester 1: Unix, Python, Logic, and a File Integrity Monitor project
  - unix_1, unix_2, python_2, logic_1, FileIntegrityMonitor
- Semester 2: Applied artifacts and planning
  - Flowcharts, algorithm design (FigJam), SOC project plan, and role research  
  foundation deck, linkedin profile, resume, IDP, feedback summary, project plan, job description, project board 
https://www.linkedin.com/in/matthew-rich-15910a196/   https://github.com/Goinghome22   https://docs.google.com/document/d/16YaTse_WIO19zznnRmGVpRbD16IVOnnjY0PCPaQjZ8Q/edit?tab=t.0
## Highlights

- Unix command-line mastery tied to real projects
- Python scripting: CLI budgeting and a Tkinter GUI
- Security automation: File Integrity Monitor (hash comparison with reporting)
- SOC and project planning artifacts

## Navigation

- See each semester folder `README.md` for detailed usage guides and module-level instructions. 


# Wazuh Installation

Use a Supported Wazuh Version

The 5.0.0 images are not available yet on Docker Hub.
Instead, use the latest stable release: 4.12.0.

Clone the matching branch of the Wazuh Docker repository:

```bash

git clone -b v4.12.0 https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker/single-node


docker-compose -f generate-indexer-certs.yml run --rm generator

```

# Generate SSL Certs

docker-compose -f generate-indexer-certs.yml run --rm generator


# Force Platform amd64

in docker-compose.yml alter to make it compatible

```yaml
platform: linux/amd64
```

```yaml

services:
  wazuh.manager:
    image: wazuh/wazuh-manager:4.12.0
    platform: linux/amd64   # 👈 add this
    ...
  wazuh.indexer:
    image: wazuh/wazuh-indexer:4.12.0
    platform: linux/amd64   # 👈 add this
    ...
  wazuh.dashboard:
    image: wazuh/wazuh-dashboard:4.12.0
    platform: linux/amd64   # 👈 add this
    ...


```



# Apply changes


```bash

docker-compose down
docker-compose up -d --build

```

Login

Use IPV4 address or `http://localhost` in url bar


Username : admin
Password: SecretPassword



Gabe

- Careful with numbers in your resume, maybe try using a google voice number
- Good set of previous work experience that clearly displays a wide range of soft skills such as leadership and communication
- Perhaps add a bit more flare to the document, make it more personal so it stands out

Javier
-Could add more hyperlinks to make it more dynamic
-The margins need to be corrected and everything should be properly aligned
-The structure could be better organized to optimize the space

Craig
-Make it easier to read
-The bulleted points could be more spread out

