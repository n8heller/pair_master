

def Make_Pair_Blocks(num_trials, num_blocks):
    
    f = open('pair_vars/block_var.txt', 'w')
    
    
    tpb = str(num_trials/num_blocks) # trials per block
    b2 = str(num_blocks/2) # half of the blocks
    b = str(num_blocks)
    
    
    # section 1
    f.write('    for ( var i = 0; i< '+b+'; i++){\n')
    f.write('      if (i < '+b2+'){\n')
    f.write('        doublet_stim[i] = [].concat(doublet_stim_f.slice(i*'+tpb+', i*'+tpb+'+'+tpb+'));\n')
    f.write('      }\n')
    f.write('      else{\n')
    f.write('        doublet_stim[i] = [].concat(doublet_stim_f.slice((i-2)*'+tpb+', (i-2)*'+tpb+'+'+tpb+'));\n')
    f.write('      }\n')
    f.write('      doublet_stim[i].push([temp[i],temp[i]]);\n')
    f.write('      doublet_stim[i] = jsPsych.randomization.repeat(doublet_stim[i],1);\n')
    f.write('    }\n')
    
    for i in range(num_blocks):
        f.write('    var test_doublet'+str(i+1)+'_stim = doublet_stim['+str(i)+'];\n')
    
    
    section2 = """
    //practice with instruction blocks
    var trial_num = 0;
    var prac_doublet_block = {
      type: 'similarity_custom',
      stimuli: prac_doublet_stim,
      text: '<div style="text-align: left; margin-top:30px;"> <p>In the <span class = "emp">Face Pair Task</span>, your need to rate how similar a face pair is from <span class="emp">1</span> to <span class="emp">9</sapn>.</p> <p><span class="emp">1</span> indicates <span class="emp">Maximally Dissimilar</span>, <span class="emp">9</span> indicates <span class="emp">Maximally Similar</span></p> <p> If you see two identical faces, please click the <span class="emp">identical</span> button.</p> <p> <em class="emp">Try to focus on the face features and ignore the pose, expression and lighting influence.</em></p></div><br><br>',
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      set_num: 1
    };
    trial_num +=1;
    var instruction_doublet_chunk = {
        chunk_type: 'while',
        timeline: [prac_doublet_block,prac1_end_block],
        continue_function: function(){
          var back_button = document.getElementById('Back').clicked;
            $('.well').remove();
            $('.jspsych-survey-text').remove();
            if( back_button){
              return true;
            }
            else{
              return false;
            } 
        }
    };
   
    //practice with no instruction blocks
    var prac_no_inst_doublet_block = {
      type: 'similarity_custom',
      stimuli: prac_no_inst_doublet_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      set_num: 1
    };

    trial_num +=1;
    """
    
    f.write(section2)
    
    # section 3, prints each block variable in five sections
    for i in range(num_blocks):
        
        b_sec1 = 'var test_doublet'+str(i+1)+'_block = {\n'+"      type: 'similarity_custom',"

        b_sec2 = 'stimuli: test_doublet'+str(i+1)+'_stim,'
      
        b_sec3 = """
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      """
        b_sec4 = 'phase: '+str(i+1)+','
        
        b_sec5 = """
      set_num:setNumber
    }; 
      """
        
        f.write(b_sec1+b_sec2+b_sec3+b_sec4+b_sec5)
    
    
    section4 = """
    var trial_chunk = {
    chunk_type: 'linear',
    
    """
    
    f.write(section4)
    
    # section 5, construct timeline
    f.write('timeline: [')
    for i in range(num_blocks-1):
        
        if i == num_blocks/2:
            f.write('break2_block,')
            
        f.write('test_doublet'+str(i+1)+'_block,')
        
    f.write('test_doublet'+str(i+2)+'_block]')    
    
    
    
    
    
    
    
    
    
    
    
    