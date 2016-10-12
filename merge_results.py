# Keep coding and change the world..And do not forget anything..Not Again..
import pickle

headings = ['Name', 'COMPUTER NETWORKS', 'DESIGN AND ANALYSIS OF ALGORITHMS', 'THEORY OF COMPUTATION',
            'COMPUTER GRAPHICS & MULTIMEDIA TECHNIQUES', 'EMBEDDED SYSTEM DESIGN',
            'ADVANCE TOPICS IN OPERATING SYSTEMS', 'JAVA PROGRAMMING LAB', 'Computer graphics & multimedia lab',
            'DESIGN AND ANALYSIS OF ALGORITHMS Lab', 'Embedded System Design Lab', 'Humanities and Social Sciences',
            'Discipline', 'All Subjects', 'Result']

data = pickle.load(open('final_result.rtu', 'rb'))
i = 1
data = sorted(data, key=lambda x: x[-2], reverse=True)
for i, item in enumerate(data):
    print i + 1, '->', item[0], item[-2]

pickle.dump(sorted(data, key=lambda x: x[0]), open('final_result.rtu', 'wb+'))
