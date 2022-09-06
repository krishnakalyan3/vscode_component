import lightning as L
from typing import Optional
import subprocess

class CustomBuildConfig(L.BuildConfig):
    def build_commands(self):
        return ["curl -fsSL https://code-server.dev/install.sh | sh"]


class VSCodeServer(L.LightningWork):
    def __init__(self, cloud_compute: Optional[L.CloudCompute] = None):
        super().__init__(cloud_compute=cloud_compute, cloud_build_config=CustomBuildConfig(), parallel=True)
        self.vscode_url = None

    def run(self):
        # Start VSCodeServer
        with open(f"/home/zeus/vscode_server_{self.port}", "w") as f:
            proc = subprocess.Popen("code-server --bind-addr '{self.host}:{self.port}' --auth none",
                bufsize=0,close_fds=True,stdout=f,stderr=f)
