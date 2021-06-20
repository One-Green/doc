from diagrams import Cluster, Diagram
from diagrams.k8s.network import SVC
from diagrams.k8s.storage import PVC
from diagrams.k8s.compute import Deploy, STS
from diagrams.k8s.clusterconfig import HPA
from diagrams.gcp.analytics import Pubsub
from diagrams.onprem.network import Nginx

INGRESSES_CLUSTER = "Ingresses"
SVC_CLUSTER = "Services"
WORKLOAD_CLUSTER = "Workloads"
MQTT = "MQTT Topics Subscribe and publish"
STORAGE_CLUSTER = "Storage"
_HPA = "Horizontal Pod AutoScaler"
MONITORING = "Monitoring"

with Diagram(
        name="One-Green Core Helm Kubernetes Architecture",
        filename="export/helm_k8s_architecture",
        show=False
):
    with Cluster(INGRESSES_CLUSTER):
        api_ingress = Nginx("API")
        admin_ui_ingress = Nginx("Admin UI")
        grafana_ingress = Nginx("Grafana")

    with Cluster(SVC_CLUSTER):
        api_svc = SVC("API")
        admin_ui_svc = SVC("Admin UI")
        pg_svc = SVC("PostgreSQL")
        influxdb_svc = SVC("InfluxDB")
        grafana_svc = SVC("Grafana")
        redis_svc = SVC("Redis")
        mqtt_svc = SVC("MQTT")

        api_ingress >> api_svc
        admin_ui_ingress >> admin_ui_svc
        grafana_ingress >> grafana_svc

    with Cluster(WORKLOAD_CLUSTER):
        api_deploy = Deploy("Django & Celery")
        admin_ui_deploy = Deploy("Streamlit UI")
        mqtt_sts = STS("MQTT broker")
        pg_sts = STS("PostgreSQL")

        api_svc >> [api_deploy, admin_ui_deploy]
        admin_ui_svc >> admin_ui_deploy
        pg_svc >> api_deploy
        mqtt_svc >> mqtt_sts

        with Cluster(MQTT):
            water_consumer_sts = STS("Water topic\n subscriber")
            sprinkler_consumer_sts = STS("Sprinkler topic\n subscriber")
            light_consumer_sts = STS("Light topic\n subscriber")
            redis_sts = STS("Redis")
            sensor_sub = Pubsub("Sensors topics\n subscriber")
            controller_publisher = Pubsub("Controller topics\n publisher")
            celery_worker_deploy = Deploy("Celery\n controller Worker")
            mqtt_svc >> sensor_sub >> \
                [water_consumer_sts, sprinkler_consumer_sts, light_consumer_sts] >> \
                redis_sts >> \
                celery_worker_deploy >> \
                controller_publisher >> \
                mqtt_sts
            redis_svc >> redis_sts

        with Cluster(MONITORING):
            telegraf_sts = STS("Telegraf")
            influxdb_sts = STS("InfluxDB")
            grafana_deploy = Deploy("Grafana")

            mqtt_svc >> telegraf_sts >> influxdb_sts >> grafana_deploy
            influxdb_svc >> influxdb_sts

    with Cluster(STORAGE_CLUSTER):
        pg_pvc = PVC("PostgreSQL")
        influxdb_pvc = PVC("InfluxDB")
        grafana_pvc = PVC("Grafana")
        redis_pvc = PVC("Redis")

        pg_sts >> pg_pvc
        influxdb_sts >> influxdb_pvc
        grafana_deploy >> grafana_pvc
        redis_pvc >> redis_sts

    with Cluster(_HPA):
        celery_worker_hpa = HPA("Celery Worker")
        celery_worker_deploy >> celery_worker_hpa
