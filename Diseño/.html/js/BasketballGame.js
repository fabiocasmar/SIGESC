			function hideRules() {
 
             $("img").fadeTo("fast", 1);
             $("img#hoop").css({'left':'75px'}); 
				 $("img#rules").hide();
             $("img#ok").hide();
				 $("div#reglas").hide();
             $("img#ball").show()
         	 $("img#brain").show();
			}
         function showRules() {
             $("img").fadeTo("fast", .5);
 				 $("img#rules").fadeTo("fast", 1);
				 $("img#ok").fadeTo("fast", 1);
				 $("img#rules").show();
				 $("img#ok").show();
             $("div#reglas").show();
             $("img#brain").hide();
             $("img#ball").hide(); 
             
				 $("img#hoop").css({'left':'170px'}); 
         }
 
         function hideResult() {
				 $("div#result").hide();
				 $("div#reglas").hide();
				 $("img#rules_button").show();
				 $("img#start_button").show();
			}

         function throwIn(question,correct) {
      		 var y=25,x=5;
             var swoosh = new Audio ("sound/swoosh2.mp3");
				 var bounce= new Audio ("sound/bounce.mp3");
 
	          for(var i = 0;i<29;i++){ //lanzamiento
 					$("img#ball").animate({left: "+="+(x), bottom: '+='+(y-i)},30);
					}
	
	          y=7
  				 for(var i = 0;i<10;i++){ // empieza a bajar y suena la malla
 					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},20);
				 }
               $("img#ball").animate({left: "=", bottom: '='},1, function () {
																				
																											swoosh.play()});
				for(var i = 10;i<25;i++){ //termina de bajar y se pasa a la 
					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},20, function () {

						$("img#ball").animate({'left':'-10px', 'bottom' :'1080px'},1,function() {bounce.play();
																													 $(question).show();
                                                                                        $(correct).hide()
                                                                                         })});
					
				}

       
			}

         function throwOut(question, correct) {
				 var y=25,x=7;
             var miss = new Audio ("sound/missed1.mp3");
				 var bounce = new Audio ("sound/bounce.mp3");
				 var cheers = new Audio ("sound/boo.mp3");
				 cheers.play();
	          for(var i = 0;i<25;i++){ // move down and move right 1 pixel at a time to get effect
 					$("img#ball").animate({left: "+="+(x), bottom: '+='+(y-i)},40);
				 }

	          y=5
    			 click.currentTime = 0;
  				 for(var i = 0;i<10;i++){ // move down and move right 1 pixel at a time to get effect
 					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},25, function () {
																										cheers.pause()}); 
				 }
               $("img#ball").animate({left: "=", bottom: '='},1, function () {
																											
																											miss.play()});
				 for(var i = 10;i<20;i++){
					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},20, function () {
						$("img#ball").animate({'left':'-10px', 'bottom' :'1080px'},1,function() { bounce.play();
																													    $(question).show();
                                                                                           $(correct).hide()})});
			
				}

			}

         function throwOut1(question, correct) {
				 var y=25,x=4;
             var miss = new Audio ("sound/missed1.mp3");
				 var bounce = new Audio ("sound/bounce.mp3");
	          for(var i = 0;i<24;i++){ // move down and move right 1 pixel at a time to get effect
 					$("img#ball").animate({left: "+="+(x), bottom: '+='+(y-i)},40);
				 }

	          y=5
  				 for(var i = 0;i<10;i++){ // move down and move right 1 pixel at a time to get effect
 					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},25); 
				 }
               $("img#ball").animate({left: "=", bottom: '='},1, function () {
																											miss.play()});
				 for(var i = 10;i<20;i++){
					$("img#ball").animate({left: "+="+(x), bottom: '-='+i},20, function () {
						$("img#ball").animate({'left':'-10px', 'bottom' :'1080px'},1,function() { bounce.play();
																													    $(question).show();
                                                                                           $(correct).hide()})});
				}
			
			}


			function answer(a) {
				$(a).show();
			}

