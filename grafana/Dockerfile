FROM grafana/grafana:latest

LABEL version "v1.0.0"
LABEL Christian Sargusingh "https://github.com/cSDes1gn"

USER grafana

ENV GF_SECURITY_ADMIN_USER "admin"
ENV GF_SECURITY_ADMIN_PASSWORD "loki"

ADD ./provisioning /etc/grafana/provisioning
ADD ./grafana.ini /etc/grafana/grafana.ini
ADD ./dashboards /var/lib/grafana/dashboards

ENTRYPOINT [ "/run.sh" ]