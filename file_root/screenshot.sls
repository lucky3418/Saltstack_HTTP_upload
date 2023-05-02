#
# salt <minion> saltutil.refresh_pillar
# salt <minion> state.apply screenshot
# salt <minion> schedule.list
# salt <minion> schedule.enable_job job_screenshot
# salt <minion> schedule.enable
#

{% for section, content in pillar.items() %}
{% if section | regex_match('screenshot(.*)', ignorecase=True) != None %}

{% set url_key = [section, 'url'] | join(':') %}
{% set url = salt.pillar.get(url_key) %}
{% set seconds_key = [section, 'seconds'] | join(':') %}
{% set seconds = salt.pillar.get(seconds_key) %}

job_{{ section }}:
  schedule.present:
    - function: screenshot.screenshot_upload
    - seconds: {{ seconds }}
    - job_args:
      - {{ url }}

{% endif %}
{% endfor %}
