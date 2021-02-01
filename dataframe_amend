# create number of data entries appropriate to fps

import pandas as pd
recordings = ['call_id_1',
              'call_id_2',
              'call_id_3',
              'call_id_4']
              
for x in recordings:
    recording_info = pd.read_csv(r'dir' + x + '.csv')
    columns = ["pred", "t_lab", "f_name", "status", "dial", "hold", "human", "message_hold", "message_init"]
    fps=15
    new_data = []
    for i in range(1, len(recording_info)):
        for a in range(fps):
            next_row = [recording_info.iloc[i]["pred"],
                         recording_info.iloc[i]["t_lab"],
                         recording_info.iloc[i]["f_name"],
                         recording_info.iloc[i]["status"],
                        1 / fps * ((recording_info.iloc[i-1]["dial"] * (fps - a)) + (recording_info.iloc[i]["dial"] * a)),
                        1 / fps * ((recording_info.iloc[i-1]["hold"] * (fps - a)) + (recording_info.iloc[i]["hold"] * a)),
                        1 / fps * ((recording_info.iloc[i-1]["human"] * (fps - a)) + (recording_info.iloc[i]["human"] * a)),
                        1 / fps * ((recording_info.iloc[i-1]["message_hold"] * (fps - a)) + (recording_info.iloc[i]["message_hold"] * a)),
                        1 / fps * ((recording_info.iloc[i-1]["message_init"] * (fps - a)) + (recording_info.iloc[i]["message_init"] * a))]
            new_data.append(next_row)
        new_data.append(recording_info.iloc[i])

    new_data = pd.DataFrame.from_records(new_data)
    new_data.columns = columns
    new_data.to_csv(r'dir' + x + '_expanded_df.csv')
