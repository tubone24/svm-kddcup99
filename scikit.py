#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import svm


col_names_data = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
                  "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
                  "num_compromised", "root_shell", "su_attempted", "num_root",
                  "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
                  "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
                  "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
                  "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
                  "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
                  "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]

kdd_data_10percent = pd.read_csv("kddcup99/kddcup.data_10_percent", header=None, names=col_names_data)


col_names_unlabel = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
                     "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
                     "num_compromised", "root_shell", "su_attempted", "num_root",
                     "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
                     "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate",
                     "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
                     "dst_host_count","dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
                     "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
                     "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate"]

kdd_data_unlabel = pd.read_csv("kddcup99/kddcup.testdata.unlabeled_10_percent", header=None, names=col_names_unlabel)

clf = svm.SVC()

clf.fit(kdd_data_unlabel, kdd_data_10percent)



