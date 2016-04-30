
# This Make_Study function will help you print out the html file that needs to be used to run the whole experiment.
def Make_Trip_Study(study_name):

    html_constant = """
<!doctype html>
<html>
 <head>
    <title>My experiment</title>
        <script type="text/javascript" src="/static/lib/jquery.js"></script>
        <script src="/static/lib/jquery-min.js" type="text/javascript"></script>
        <script src="/static/lib/bootstrap.min.js" type="text/javascript"></script>
        <script src="/static/lib/underscore-min.js" type="text/javascript"></script>
        <script src="/static/lib/backbone-min.js" type="text/javascript"></script>   
        <script src="/static/js/myjspsych/jspsych.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-text.js" type="text/javascript"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-similarity.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-similarity-custom.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-custom-triplet.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-text.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-survey-select.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-survey-text.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-survey-new.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-call-function.js" type="text/javascript"></script>
        <script src="/static/js/myjspsych/plugins/jspsych-html.js" type="text/javascript"></script>        
        
        <!-- utils.js and psiturk.js provide the basic psiturk functionality -->
        <script src="/static/js/utils.js" type="text/javascript"></script>
        <script src="/static/js/psiturk.js" type="text/javascript"></script>
        
        <link href="/static/js/myjspsych/css/jspsych.css" rel="stylesheet" type="text/css"></link>
        <link href="/static/css/style.css" rel="stylesheet" type="text/css"></link>
        <link href="/static/css/bootstrap.min.css" rel="stylesheet" type="text/css"></link>
        <link href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/black-tie/jquery-ui.min.css" rel="stylesheet" type="text/css"></link>
  </head>
  
  <body>
        <div id="jspsych_target" class="jspsych_target"></div>
  </body>
  <script>
  
    // These fields provided by the psiTurk Server
    var uniqueId = "{{ uniqueId }}"; // a unique string identifying the worker/task
    //console.log(typeof uniqueId);
    var ids = uniqueId.split(":"); 
    var workerId = ids[0];
    var assignmentId = ids[1];
    var adServerLoc = "{{ adServerLoc }}"; // the location of your ad (so you can send user back at end of experiment)
    var mode = "{{ mode }}"; // is this running live, sandbox, or in debug mode?
/*   
    htmlobj = $.ajax({
      url: "http://52.24.142.90/update_counter.php",
      async: false,
      method: "POST",
      data: { assignmentID: assignmentId, workerID: workerId, hitID: '3'}
    });
    console.log('Updated counter: ' + htmlobj.responseText);


    htmlobj = $.ajax({
      url: "http://52.24.142.90/give_counter.php",
      async: false,
      method: "POST",
      data: { assignmentID: assignmentId, workerID: workerId, hitID: '3'}
    });
    var outputCounter = htmlobj.responseText;
    console.log('Current counter: ' + outputCounter);
    var counter = parseInt(outputCounter.split(' ')[3]);

*/
        //read a text file
    function readTextFile(file){
       htmlobj=$.ajax({url:file,async:false});
       var list = htmlobj.responseText;
       var listArray = list.split(/\\n/g);
       for (a in listArray ) {
           listArray[a] = listArray[a].split(","); 
           for( b in listArray[a]){
             listArray[a][b] = '/static/images/img/' + listArray[a][b];
           }
       }
       listArray = listArray.slice(0,listArray.length-1);
       return listArray;
   }

    var post_trial_gap = function() {
      return Math.floor( Math.random() * 750 );
    }

    var question_age = ["My age is"];
    var welcome_survey_new_block = {
      type: "survey_new",
      questions: [question_age],
      text: "<div class='jspsych_target jspsych-display-element' style='text-align: left; width: 500px; margin-left: 30% auto; padding-top: 30px'> <div class='jspsych-survey-likert-preamble'>Please fill out this short survey </div> <div class='jspsych-survey-text-question'> <p class='jspsych-survey-text'> My gender is <br> <input type='radio' name='gender' id='Female' value='1'> <label for='Female'> Female</label> <br> <input type='radio' name='gender' id='Male' value='2'> <label for='Male'> Male</label> <br> <input type='radio' name='gender' id='Other' value='0'> <label for='Other_gender'> Other</label> <br> <!--<input type='radio' name='gender' id='no_say' value='3'><label for='No_say'> I prefer not to disclose this information</label><br>--> </p> </div> <div class='jspsych-survey-text-question'> <p class='jspsych-survey-text'> My race / ethnicity is (select one or more) <br> <input type='checkbox' name='race' id='race American Indian or Alaska Native' value='1'> <label for='race American Indian or Alaska Native'> American Indian or Alaska Native</label> <br> <input type='checkbox' name='race' id='race Asian' value='2'> <label for='race Asian'> Asian</label> <br> <input type='checkbox' name='race' id='race Black or African American' value='3'> <label for='race Black or African American'> Black or African American </label> <br> <input type='checkbox' name='race' id='Hispanic' value='4'> <label for='Hispanic'> Hispanic </label> <br> <input type='checkbox' name='race' id='race Native Hawaiian or Other Pacific Islander' value='5'> <label for='race Native Hawaiian or Other Pacific Islander'> Native Hawaiian or Other Pacific Islander </label> <br> <input type='checkbox' name='race' id='race White_Not_Hispanic' value='6'> <label for='race White_Not_Hispanic'> White / Not Hispanic </label> <br> <input type='checkbox' name='race' id='race Other' value='0'> <label for='race Other'> Other</label> <br> <!--<input type='checkbox' name='race' id='no_say' value='7'><label for='No_say'> I prefer not to disclose this information</label><br>--> </p> </div> <div class='jspsych-survey-text-question'> <p class='jspsych-survey-text'> The races / ethnicities of people in the communities I've lived in are (select one or more) <br> <input type='checkbox' name='comRace' id='comRace American Indian or Alaska Native' value='1'> <label for='comRace American Indian or Alaska Native'> American Indian or Alaska Native</label> <br> <input type='checkbox' name='comRace' id='comRace Asian' value='2'> <label for='comRace Asian'> Asian</label> <br> <input type='checkbox' name='comRace' id='comRace Black or African American' value='3'> <label for='comRace Black or African American'> Black or African American </label> <br> <input type='checkbox' name='comRace' id='comRace Hispanic' value='4'> <label for='comRace Hispanic'> Hispanic </label> <br> <input type='checkbox' name='comRace' id='comRace Native Hawaiian or Other Pacific Islander' value='5'> <label for='comRace Native Hawaiian or Other Pacific Islander'> Native Hawaiian or Other Pacific Islander </label> <br> <input type='checkbox' name='comRace' id='comRace White_Not_Hispanic' value='6'> <label for='comRace White_Not_Hispanic'> White / Not Hispanic </label> <br> <input type='checkbox' name='comRace' id='comRace Other' value='0'> <label for='comRace Other'> Other</label> <br> <!--<input type='checkbox' name='comRace' id='no_say' value='7'><label for='No_say'> I prefer not to disclose this information</label><br>--> </p> </div> <div class='jspsych-survey-text-question'> <p class='jspsych-survey-text'> My sexual orientation is <br> <input type='radio' name='sexual_ori' id='Bisexual' value='1'> <label for='Bisexual'> Bisexual</label> <br> <input type='radio' name='sexual_ori' id='Heterosexual' value='2'> <label for='heterosexual'> Heterosexual</label> <br> <input type='radio' name='sexual_ori' id='Homosexual' value='3'> <label for='Homosexual'> Homosexual</label> <br> <input type='radio' name='sexual_ori' id='Other' value='0'> <label for='Other'> Other</label> <br> <input type='radio' name='sexual_ori' id='no_say' value='4'> <label for='No_say'> I prefer not to disclose this information</label> </p> </div></div>"
    };
   
    var face_images_explore_ready_block = {
      type: "text",
      text: '<div> <h2 class="emp"> Face Similarities Test</h2> <hr> <div class="well"> <p>In this HIT, your task is to judge the similarities between faces.</p> <div class="row"> <div class="col-md-12"> <h5><b>Face Triplet Task</b></h5> <p> You will see 3 faces. <b>Click on the two faces that you think are most similar</b> to each other. </p> <img src="/static/images/faceExamples/trial2.png" style="width:100%" /> </div> </div> <p style="margin-bottom: 30px;">We will walk you through the task. </p> <p>First, you will see some <span class="emp">face examples</span>.</p> <p>Next there will be a <span class="emp">practice session </span> to warm you up.</p> <p>Then comes the <span class="emp">actual task</span>. You will be the judge of various faces!</p> </div></div>',
      timing_post_trial: post_trial_gap
    };

    var face_images_explore_block4 = {
      type: "text",
      text: "<div class='im'><h3>Face Examples (1/3)</h3> <hr> <img src='/static/images/faceExamples/femaleExp1.jpg' style='width:100%'/> <br></div> ",
      skip_button: true,
      loop_num: 0,
      on_finish: function(){
                if(this.loop_num++ > 0){
                  var skip = document.getElementById('Skip').clicked;
                  $('.well').remove();
                  $('.jspsych-survey-text').remove();
                  if(skip){
                    jsPsych.endCurrentChunk();
                  }
                }
                
              },
      timing_post_trial: post_trial_gap
    };
    var face_images_explore_block5 = {
      type: "text",
      text: "<div class='im'><h3>Face Examples (2/3)</h3> <hr> <img src='/static/images/faceExamples/femaleExp2.jpg' style='width:100%'/> <br> </div> ",
      skip_button: true,
      loop_num: 0,
      on_finish: function(){
                if(this.loop_num++ > 0){
                  var skip = document.getElementById('Skip').clicked;
                  $('.well').remove();
                  $('.jspsych-survey-text').remove();
                  if(skip){
                    jsPsych.endCurrentChunk();
                  }
                }
                
              },
      timing_post_trial: post_trial_gap
    };
    var face_images_explore_block6 = {
      type: "text",
      text: "<div class='im'><h3>Face Examples (3/3)</h3> <hr> <img src='/static/images/faceExamples/femaleExp3.jpg' style='width:100%'/> <br> </div> ",
      skip_button: true,
      loop_num: 0,
      on_finish: function(){
                if(this.loop_num++ > 0){
                  var skip = document.getElementById('Skip').clicked;
                  
                  if(skip){
                    $('.im').remove();
                    $('.jspsych-survey-text').remove();
                    jsPsych.endCurrentChunk();
                  }
                }
                
              },
      timing_post_trial: post_trial_gap
    };

    var face_images_explore_end_block = {
      type: "text",
      text: '<div class="well"> <p>If you wish to see the face examples again, click  <span class="emp">Go Back</span>.</p> <p>Otherwise, click <span class="emp">Continue</span> to proceed.</p><br></div>',
      back_button: true,
      timing_post_trial: post_trial_gap
    };

    var face_example_chunk = {
        chunk_type: 'while',
        timeline: [face_images_explore_block4,face_images_explore_block5,face_images_explore_block6,face_images_explore_end_block],
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
    var bad_examples_ready_block = {
        type: "text",
        text: '<div class="well"> <p>Good Job! </p> <p> Now you know what the task is.</p> <p> Keep in mind that you should <span class="emp"> focus on the faces themselves </span> rather then the pose, expression and lighting condition of the faces.</p> <p> We will show you two examples of what you should pay attention to.</p><br></div>',
        timing_post_trial: post_trial_gap
      };
    var bad_examples_block1 = {
        type: "text",
        text:"<div class = 'title'><h3>Focus on Faces rathar than Poses</h3> <hr> <div class='well'> <p>In Figure 1, you should choose the top and left faces even though the bottom two faces have similar poses. </p><p>In Figure 2, you should choose the top and right faces even though the two bottom faces have similar poses.</p> <br> <div class='row'> <div class='col-md-6'>  <img src='/static/images/bad_examples/f1bad.JPG' style='width:100%'/> <p>Figure 1</p></div> <div class='col-md-6'> <img src='/static/images/bad_examples/m1bad.JPG' style='width:100%'/><p>Figure 2</p> </div> </div></div></div>",
        skip_button: true,
        loop_num: 0,
        on_finish: function(){
                  if(this.loop_num++ > 0){
                    var skip = document.getElementById('Skip').clicked;
                    $('.well').remove();
                    $('.title').remove();
                    $('.jspsych-survey-text').remove();
                    if(skip){
                      jsPsych.endCurrentChunk();
                    }
                  }
                  
                },
        timing_post_trial: post_trial_gap
     };
     var bad_examples_block2 = {
       type: "text",
       text:"<div class = 'title'><h3>Focus on Faces rather than Expressions</h3> <hr> <div class='well'> <p>In Figure 1, you should choose the two faces at the bottom even though the top and left faces have similar expressions. </p> <p>In Figure 2, you should choose the top face and the left face even though the two faces on the bottom are of similar expressions.</p> <br> <div class='row'> <div class='col-md-6'>  <img src='/static/images/bad_examples/f2bad.JPG' style='width:100%'/> <p>Figure 1</p></div> <div class='col-md-6'> <img src='/static/images/bad_examples/m2bad.JPG' style='width:100%'/><p>Figure 2</p> </div> </div></div></div>",
        skip_button: true,
        loop_num: 0,
        on_finish: function(){
                  if(this.loop_num++ > 0){
                    var skip = document.getElementById('Skip').clicked;
                    $('.well').remove();
                    $('.title').remove();
                    $('.jspsych-survey-text').remove();
                    if(skip){
                      jsPsych.endCurrentChunk();
                    }
                  }
                  
                },
       timing_post_trial: post_trial_gap
     }
     var bad_examples_end_block = {
      type: "text",
      text: '<div class="well"> <p>If you wish to see the examples again, click  <span class="emp">Go Back</span>.</p> <p>Otherwise, click <span class="emp">Continue</span> to have some <span class="emp">warm up practices</span>. </p><br></div>',
      back_button: true,
      timing_post_trial: post_trial_gap
    };
    var bad_examples_chunk = {
        chunk_type: 'while',
        timeline: [bad_examples_block1,bad_examples_block2,bad_examples_end_block],
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
    var prac1_end_block = {
      type: "text",
      text: '<div class="well"> <p>If you wish to read the previous instructions again, click  <span class="emp">Go Back</span>.</p> <p>Otherwise, click <span class="emp">Continue</span> to proceed.</p><br></div>',
      back_button: true,
      timing_post_trial: post_trial_gap
    };
 
    var prac_no_inst_ready_block = {
      type: "text",
      text: '<div class="well"> <p> Now you are half way prepared. Practice a few more.</p> <br> </div>',
      timing_post_trial: post_trial_gap
    };

    var test_ready_block = {
      type: "text",
      text: "<div class='well'><br><p style='text-align: center; font-weight: bold; color: #3f6479; font-size: 24px;'> Great Job! :) </p><br><p>Now you are ready for the actual trials!</p><p> You will be presented with around 200 trials separated in four phases. It'll be the same task as what you just practiced, except that there are instructions between trials. There will be a short break in the half way point.</p>  <p>Remember the most important rule: <strong style='color: #3f6479;'><em> Go with your gut and respond consistently!</em></strong></p> <p>When you're ready, press the <b>Start Experiment</b> button below to begin the test. </p><br></div>",
      cont: 'Start Experiment',
      timing_post_trial: post_trial_gap
    };

    var break2_block = {
      type: "text",
      text: '<div class="well"><p class="emp">Well done!</p> <p>You have finished 1/2 of the experiment. Take a short break!</p> <p>Click <span class="emp">Continue</span> when you are ready to proceed. </p> <br></div>',
      timing_post_trial: post_trial_gap
    };

    var complete_block = {
      type: "text",
      text: '<div class="well"><p class="emp" style="font-size: 24px;">Thank you for your participation!</p> <p>You have finished the whole experiment.</p><br></div>',
      timing_post_trial: post_trial_gap
    };


    /* define test block */
    var counter =90;
    var setNumber = counter;
    var repNumber = counter%5+1;
    var doublet_stim_f = readTextFile("https://raw.githubusercontent.com/amandasongmm/filesPublic/master/august/doubletPilot.txt");
    var triplet_iostim_f = readTextFile("https://raw.githubusercontent.com/amandasongmm/filesPublic/master/oct_triplet_only/tri_set" + setNumber.toString() + '.txt');
    var prac_doublet_stim_f = readTextFile("https://raw.githubusercontent.com/amandasongmm/filesPublic/master/sampleMethod1/sampleMethod1_set10rep1.txt");
    var prac_triplet_stim_f = readTextFile("https://raw.githubusercontent.com/amandasongmm/filesPublic/master/august/tripletPractice.txt");
    function getAllImages() {
      var images = []
      images = images.concat(prac_doublet_stim_f);
      images = images.concat(prac_triplet_stim_f);
      images = images.concat(doublet_stim_f);
      images = images.concat(triplet_stim_f);
      return images;
    }
    
    var prac_doublet_stim = [prac_doublet_stim_f[0]];
    var prac_triplet_stim = [prac_triplet_stim_f[0]];
    var prac_no_inst_doublet_stim = prac_doublet_stim_f.slice(2,4);
    var prac_no_inst_triplet_stim = prac_triplet_stim_f.slice(2,4);


    function getRandomInt (min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    //catchy question
    max = prac_triplet_stim_f.length;
    var catchy_index = getRandomInt (1, max);
    var doublet_catchy = []
    var triplet_catchy = []
    var doublet_stim = []
    var triplet_stim = []
    var temp = prac_triplet_stim_f[catchy_index];
    temp.push(prac_triplet_stim_f[catchy_index+1][0]);
    max = prac_doublet_stim_f.length;

    for ( var i = 0; i< 4; i++){
      catchy_index = getRandomInt (0, max);
      doublet_stim[i] = [].concat(doublet_stim_f);
      triplet_stim[i] = [].concat(triplet_stim_f.slice(i*50, i*50+50));
      doublet_stim[i].push([temp[i],temp[i]]);
      triplet_stim[i].push(prac_doublet_stim_f[catchy_index]);
      doublet_stim[i] = jsPsych.randomization.repeat(doublet_stim[i],1);
      triplet_stim[i] = jsPsych.randomization.repeat(triplet_stim[i],1);
    }
    //var test_doublet1_stim = doublet_stim[0].concat(doublet_stim[3]);
    //var test_doublet2_stim = doublet_stim[1].concat(doublet_stim[2]);
    var test_triplet1_stim = triplet_stim[0];
    var test_triplet2_stim = triplet_stim[1];
    var test_triplet3_stim = triplet_stim[2];
    var test_triplet4_stim = triplet_stim[3];
    console.log(triplet_stim);

    /*test_doublet1_stim = test_doublet1_stim.slice(0,2);
    test_doublet2_stim = test_doublet2_stim.slice(0,2);
    test_triplet2_stim = test_triplet2_stim.slice(0,2);
    test_triplet3_stim = test_triplet3_stim.slice(0,2);
    test_triplet4_stim = test_triplet4_stim.slice(0,2);
    test_triplet1_stim = test_triplet1_stim.slice(0,2);*/

    //practice with instruction blocks
    var trial_num = 0;
    var prac_doublet_block = {
      type: 'similarity_custom',
      stimuli: prac_doublet_stim,
      text: '<div style="text-align: left; margin-top:30px;"> <p>This is an example of a <span class = "emp">Face Pair Task</span>, your need to rate how similar a face pair is from <span class="emp">1</span> to <span class="emp">9</sapn>.</p> <p><span class="emp">1</span> indicates <span class="emp">Maximally Dissimilar</span>, <span class="emp">9</span> indicates <span class="emp">Maximally Similar</span></p> <p> If you see two identical faces, please click the <span class="emp">identical</span> button.</p> <p> <em class="emp">Try to focus on the face features and ignore the pose, expression and lighting influence.</em></p></div><br><br>',
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
    var prac_triplet_block = {
      type: 'custom_triplet',
      stimuli: prac_triplet_stim,
      text: '<div style="text-align: left; margin-top:30px;"> <p>This is an example of a <span class="emp">Face Triplet Task</span>, you need to <span class="emp">click on the two images</span> that look most similar to you.</div>',
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      set_num: 1
    };
    var instruction_triplet_chunk = {
        chunk_type: 'while',
        timeline: [prac_triplet_block,prac1_end_block],
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
    var prac_no_inst_triplet_block = {
      type: 'custom_triplet',
      stimuli: prac_no_inst_triplet_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      set_num: 1
    };
    trial_num +=1;
    phase_num  = 1;
    //test blocks
    var test_triplet1_block = {
      type: 'custom_triplet',
      stimuli: test_triplet1_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      phase: phase_num,
      set_num:setNumber
    };  
    phase_num +=1;
    var test_triplet2_block = {
      type: 'custom_triplet',
      stimuli: test_triplet2_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      phase: phase_num,
      set_num:setNumber
    };
    phase_num +=1;

    var test_triplet3_block = {
      type: 'custom_triplet',
      stimuli: test_triplet3_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      phase: phase_num,
      set_num:setNumber
    };
    phase_num +=1;
    var test_triplet4_block = {
      type: 'custom_triplet',
      stimuli: test_triplet4_stim,
      timing_post_trial: post_trial_gap,
      trial_num: trial_num,
      phase: phase_num,
      set_num:setNumber
    };

    var trial_chunk = {
    chunk_type: 'linear',
    // timeline: [test_triplet1_block, test_doublet1_block,test_triplet2_block,break2_block,test_doublet2_block,test_triplet3_block,test_triplet4_block]
    timeline: [test_triplet1_block, test_triplet2_block,break2_block,test_triplet3_block,test_triplet4_block]
    }

    /* create experiment definition array */

    var experiment = [];
    experiment.push(face_images_explore_ready_block);
    experiment.push(face_example_chunk);
    // experiment.push(instruction_doublet_chunk);
    experiment.push(instruction_triplet_chunk);
    experiment.push(bad_examples_ready_block);
    experiment.push(bad_examples_chunk);
    // experiment.push(prac_no_inst_doublet_block);
    experiment.push(prac_no_inst_triplet_block);
    experiment.push(test_ready_block);
    experiment.push(trial_chunk);
    experiment.push(welcome_survey_new_block);
    experiment.push(complete_block);

    //start();
    jsPsych.preloadImages(getAllImages(), start)
    var psiturk = new PsiTurk(uniqueId, adServerLoc, mode);

    /* start the experiment */
    function start() {
      jsPsych.init({
        display_element: $('#jspsych_target'),
        experiment_structure: experiment,
        show_progress_bar: true,
        on_finish: function() {
            psiturk.saveData({
                success: function() { psiturk.completeHIT(); }
            });
        },
        on_data_update: function(data) {
            psiturk.recordTrialData(data);
        }
      });
    }
  </script>
</html>
        """

            
    new_trip = html_constant

    f = open(study_name + "_exp.html","w")
    f.write(new_trip)
    f.close()
    return

