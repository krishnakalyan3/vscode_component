#!/usr/bin/env python3

import os
import lightning as L
from lit_vscode import VSCodeServer

class RootFlow(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.vscode_work = VSCodeServer(cloud_compute=L.CloudCompute(os.getenv("COMPUTE", "cpu-small")))

    def run(self):
        self.vscode_work.run()
    
    def configure_layout(self):
        return [{'name': "VSCode", 'content': self.vscode_work}]

app = L.LightningApp(RootFlow())
