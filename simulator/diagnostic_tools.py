ROOTS=["dns","routing","load_balancer","firewall","server","application"]
TOOL_COMPONENT={"dig":"dns","traceroute":"routing","avi_lookup":"load_balancer","firewall_check":"firewall","server_health":"server","application_health":"application"}

def likelihoods(tool):
    target=TOOL_COMPONENT[tool]
    # Strong signal for matching root cause, small false-positive probability otherwise.
    return {r:(0.92 if r==target else 0.08) for r in ROOTS}

def execute(tool, incident):
    target=TOOL_COMPONENT[tool]
    abnormal = incident["root_cause"] == target
    messages={
      "dig": ("DNS resolution failed","DNS resolution healthy"),
      "traceroute": ("Network path failure detected","Network path reachable"),
      "avi_lookup": ("Load-balancer/backend pool unhealthy","Load-balancer healthy"),
      "firewall_check": ("Firewall policy/path block detected","Firewall path allowed"),
      "server_health": ("Server/backend health failure","Server health normal"),
      "application_health": ("Application health failure","Application health normal")}
    return {"tool":tool,"abnormal":abnormal,"observation":messages[tool][0 if abnormal else 1]}
