******************************
Setup MicroK8s on Raspberry Pi
******************************

To deploy One-Green Core, we need to setup **Microk8s** on Raspberry Pi.

.. note::

  MicroK8s is a lightweight distribution of Kubernetes.

  Kubernetes is a container orchestration tool, that allow you to easily manage workload, network, storage, and more.

  Microk8S official documentation: https://microk8s.io/docs

  k8s = kube = Kubernetes, official documentation https://kubernetes.io


Hardware requirements:
 - Raspberry PI 4 B board (4CPU, 4GB) less resource is not suitable
 - At least 20Gi SD Card

The core stack deployment is based on Kubernetes, for that we install MicroK8s on Raspberry Pi.

Check cmdline.txt
-----------------

.. warning::

  If **cmdline.txt** do not contain **cgroup_enable=memory cgroup_memory=1** MicroK8s will not work well.
  You will get error such as : Node Not Ready or unable to schedule pod.


Check if **cmdline.txt** contain **cgroup_enable=memory cgroup_memory=1**

.. code-block:: shell

   if ! grep -q "cgroup_enable=memory cgroup_memory=1" "/boot/firmware/cmdline.txt";
    then echo "cmdline.txt is not good ! edit by using \"sudo vim /boot/firmware/cmdline.txt\" to append cgroup_enable=memory cgroup_memory=1 at the end of line"
    else echo "cmdline.txt is good"
   fi

If OK go to next step.

If not edit by using :

.. code-block:: shell

    sudo vim /boot/firmware/cmdline.txt
    # append without double quote "cgroup_enable=memory cgroup_memory=1" at the end of line
    sudo reboot


.. warning::

    Reboot is required

Update firewall rules
---------------------

.. code-block:: shell

    sudo ufw allow in on cni0 && sudo ufw allow out on cni0
    sudo ufw default allow routed

Install Microk8s
----------------

One line command to install, this operation can take ~10 min.
Change **--channel=xx** by updated version provided by Canonical https://microk8s.io/docs

.. code-block:: shell

    sudo snap install microk8s --classic --channel=1.19
    # outputs will be like :
    # Download snap "microk8s" (1884) from channel "1.19" ............. 26% 1.74MB/s 1m18s
    # Setup snap "microk8s" (1884) security profiles                                                                                                                              /
    # Run install hook of "microk8s" snap if present                                                                                                                              \
    # microk8s (1.19/stable) v1.19.6 from Canonical✓ installed

Install Microk8s addons
-----------------------

Enable dns, local persistant storage provider, helm and nginx loadbalancer

This operation can take ~15 min.

.. code-block:: shell

    sudo microk8s enable dns storage helm3 ingress
    # outputs will be like:
    # Enabling DNS
    # Applying manifest
    # serviceaccount/coredns created
    # configmap/coredns created
    # deployment.apps/coredns created
    # service/kube-dns created
    # clusterrole.rbac.authorization.k8s.io/coredns created
    # clusterrolebinding.rbac.authorization.k8s.io/coredns created
    # Restarting kubelet
    # DNS is enabled
    # Enabling default storage class
    # deployment.apps/hostpath-provisioner created
    # storageclass.storage.k8s.io/microk8s-hostpath created
    # serviceaccount/microk8s-hostpath created
    # clusterrole.rbac.authorization.k8s.io/microk8s-hostpath created
    # clusterrolebinding.rbac.authorization.k8s.io/microk8s-hostpath created
    # Storage will be available soon
    # Enabling Helm 3
    # Fetching helm version v3.0.2.
    #   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    #                                  Dload  Upload   Total   Spent    Left  Speed
    # 100 10.3M  100 10.3M    0     0   736k      0  0:00:14  0:00:14 --:--:-- 1680k
    # Helm 3 is enabled
    # Enabling Ingress
    # namespace/ingress created
    # serviceaccount/nginx-ingress-microk8s-serviceaccount created
    # clusterrole.rbac.authorization.k8s.io/nginx-ingress-microk8s-clusterrole created
    # role.rbac.authorization.k8s.io/nginx-ingress-microk8s-role created
    # clusterrolebinding.rbac.authorization.k8s.io/nginx-ingress-microk8s created
    # rolebinding.rbac.authorization.k8s.io/nginx-ingress-microk8s created
    # configmap/nginx-load-balancer-microk8s-conf created
    # configmap/nginx-ingress-tcp-microk8s-conf created
    # configmap/nginx-ingress-udp-microk8s-conf created
    # daemonset.apps/nginx-ingress-microk8s-controller created
    # Ingress is enabled

Wait until Microk8s is ready
----------------------------

.. code-block:: shell

    sudo microk8s status --wait-ready
    # if microk8s is ready, you should get :
    #microk8s is running
    #high-availability: no
    #  datastore master nodes: 127.0.0.1:19001
    #  datastore standby nodes: none
    #addons:
    #  enabled:
    #    dns                  # CoreDNS
    #    ha-cluster           # Configure high availability on the current node
    #    helm3                # Helm 3 - Kubernetes package manager
    #    ingress              # Ingress controller for external access
    #    storage              # Storage class; allocates storage from host directory
    #  disabled:
    #    dashboard            # The Kubernetes dashboard
    #    helm                 # Helm 2 - the package manager for Kubernetes
    #    host-access          # Allow Pods connecting to Host services smoothly
    #    linkerd              # Linkerd is a service mesh for Kubernetes and other frameworks
    #    metallb              # Loadbalancer for your Kubernetes cluster
    #    metrics-server       # K8s Metrics Server for API access to service metrics
    #    rbac                 # Role-Based Access Control for authorisation
    #    registry             # Private image registry exposed on localhost:32000
