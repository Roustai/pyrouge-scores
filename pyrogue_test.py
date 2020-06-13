from pyrouge import Rouge155

r = Rouge155()
r.system_dir = '/home/alex/rouge_test/Bert_Default_Summary'
r.model_dir = '/home/alex/rouge_test/gold_standard_update'
system_output_dir = '/home/alex/rouge_test/system_output'
model_output_dir = '/home/alex/rouge_test/model_output'

#file_name = ['Bed004', 'Bed009', 'Bed016', 'Bmr005', 'Bmr019', 'Bro018']


r.system_filename_pattern = 'generated.(\d+).txt'
r.model_filename_pattern = 'gold_standard.[A-Z].#ID#.txt'



output = r.convert_and_evaluate(rouge_args= '-e /home/alex/pyrouge/rouge/tools/ROUGE-1.5.5/data -c 95 -n 2 -a -s -m -2 4 -u')
print(output)
#output_dict = r.output_to_dict(output)
