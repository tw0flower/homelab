# tw0flower's homelab
This project is an attempt to automate the creation of self-hosted services all the way from basic OS provisioning the basic OS to deploying the end-user applications.

This project was inspired by [Khue's Homelab](https://github.com/khuedoan/homelab) and you should really check his project. As of now it differs on the following points:
- Dedicated identity management system running FreeIPA
- Fedora CoreOS is used instead of Fedora Server, allowing for [atomic updates](https://docs.fedoraproject.org/en-US/fedora-coreos/auto-updates/) and easy rollbacks.
- Rocky Linux is used to provision the FreeIPA system
- Podman is used instead of Docker
- iPXE is used to bootstrap both Fedora CoreOS and Rocky Linux
- TFTP is used only to load iPXE's EFI module, the rest is done through HTTPS, leading to better performances (especially if you're using Wi-Fi)

# Goals
- [x] PXE boot using temporary Podman containers ([code](https://github.com/tw0flower/homelab/tree/main/metal_provisioning/roles/netboot))
- [x] Teardown of containers
- [ ] Basic OS provisioning
- [ ] K3S cluster deployment
- [ ] Internal and external services separation
- [ ] Keycloak SSO
- [ ] Control reboot of Fedora Core OS nodes using [airlock](https://github.com/coreos/airlock)
