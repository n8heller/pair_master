

def Make_Pair_Exp(study_name, num_trials, num_blocks):
    
    Make_Pair_Blocks(num_trials, num_blocks)

    exp_f = open(study_name + '_exp.html','w')
    const1_f = open('pair_vars/pair_const1.txt','r')
    const2_f = open('pair_vars/pair_const2.txt','r')
    blocks_f = open('pair_vars/block_var.txt','r')
    
    for line in const1_f:
        exp_f.write(line)
        
    for line in blocks_f:
        exp_f.write(line)

    for line in const2_f:
        exp_f.write(line)        
        
    exp_f.close()
    const1_f.close()
    const2_f.close()
    blocks_f.close()
    return

