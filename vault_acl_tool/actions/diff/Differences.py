class Differences:
    def __init__(self):
        self._delete_policies = []
        self._update_policies = []

    def update_policy_content(self, type, name, content):
        self._update_policies.append({"%s/%s" %(type, name): content})

    def delele(self,type, name):
        self._delete_policies.append("%s/%s" %(type, name))

    def update_policies(self):
        return self._update_policies

    def delete_policies(self):
        return self.delete_policies()