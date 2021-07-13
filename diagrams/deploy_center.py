import os
from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.custom import Custom

ansible_logo_path = os.path.join(os.getcwd(), "resources", "ansible.png")
kubernetes_logo_path = os.path.join(os.getcwd(), "resources", "kubernetes.png")
helm_logo_path = os.path.join(os.getcwd(), "resources", "helm.png")
streamlit_logo_path = os.path.join(os.getcwd(), "resources", "streamlit.png")
opi_zero_path = os.path.join(os.getcwd(), "resources", "orange_pi_zero.jpeg")
raspi_4_path = os.path.join(os.getcwd(), "resources", "raspberry_pi_4.png")

platform_io_logo_path = os.path.join(os.getcwd(), "resources", "platform_io.png")
esp32_path = os.path.join(os.getcwd(), "resources", "esp32.png")
arduino_nano_path = os.path.join(os.getcwd(), "resources", "arduino_nano.png")
arduino_mega_pro_path = os.path.join(os.getcwd(), "resources", "arduino_mega_pro.png")

with Diagram(
        name="One-Green Deploy Center",
        filename="export/deploy_center",
        direction="LR",
        show=False
):
    streamlit = Custom("Webapp", streamlit_logo_path)

    with Cluster("Ansible deployment"):
        ansible = Custom("Ansible", ansible_logo_path)
        iot_edge_agent = Python("Edge IoT Agent\n Deployment")
        opi_zero = Custom("\nOrange Pi Zero LTS", opi_zero_path)
        streamlit >> ansible >> iot_edge_agent >> opi_zero

        kube_setup = Custom("Kubernetes\nSetup", kubernetes_logo_path)
        helm_deploy = Custom("Helm\nDeployment", helm_logo_path)
        raspi_4 = Custom("Raspberry 4", raspi_4_path)
        streamlit >> ansible >> [kube_setup, helm_deploy] >> raspi_4

    with Cluster("Platform deployment"):
        platform_io = Custom("PlatfromIO Core \nbuild and flash firmware", platform_io_logo_path)
        esp32 = Custom("Esp32\nplatform", esp32_path)
        arduino_nano = Custom("Arduino Nano\nplatform", arduino_nano_path)
        arduino_mega_pro = Custom("Arduino Mega pro\nplatform ", arduino_mega_pro_path)
        streamlit >> platform_io >> [esp32, arduino_nano, arduino_mega_pro]
