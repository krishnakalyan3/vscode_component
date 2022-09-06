<div align="center">
<img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_1440/https://ubuntu.com/wp-content/uploads/c9f4/visualstudio_code-card.png" width="200px">

A Lightning component to Launch Jupyter Lab
______________________________________________________________________

### [VSCodeServer](https://github.com/coder/code-server)

A Component to run Visual Studio Code Server and access it in your browser.

### Usage


```
from lit_vscode import VSCodeServer
import lightning as L
import os

class RootFlow(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.vscode_work = VSCodeServer(cloud_compute=L.CloudCompute(os.getenv("LIGHTNING_JUPYTER_LAB_COMPUTE", "cpu-small")))

    def run(self):s
        self.vscode_work.run()
    
    def configure_layout(self):
        return [{'name': "VSCode", 'content': self.vscode_work}]

app = L.LightningApp(RootFlow())
```

By default this component launches with cpu-small [Compute](https://lightning.ai/lightning-docs/core_api/lightning_work/compute.html) Instance and python Kernel. This can be overridden using the LIGHTNING_JUPYTER_LAB_KERNEL environment variable.

```
lightning run app demo_app.py --cloud
lightning run app demo_app.py --cloud --env LIGHTNING_JUPYTER_LAB_COMPUTE=gpu
```

### TODO
- [ ] Unit Test
- [ ] Application Check
- [ ] CI Pipeline
- [ ] Precommit

