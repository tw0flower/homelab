FROM rockylinux:9

RUN dnf -y install dnsmasq
COPY dnsmasq.conf /etc/dnsmasq.conf
RUN mkdir -p /var/lib/tftpboot

CMD ["dnsmasq", "-k"]
