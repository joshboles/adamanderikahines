$(document).ready(function(){
    if(location.pathname == "/"){
        $('#content').addClass("tree");
    }

    // Only do this stuff if on RSVP page
    if(location.pathname == "/rsvp/"){
        // Counter used for adding guests
        var additionalGuests = 0;
        $("[name=dinnerchoice_set-TOTAL_FORMS]").val(1);
        
        /**************************************************
         * Hide elements on page that aren't initially used
         **************************************************/
         function hideEverything(){
             
             additionalGuests = 0;
             
            $("#addGuest").addClass("hidden");
            $("#removeGuest").addClass("hidden");
            $("#dinner_descriptions").addClass("hidden");
            
            // Initial recipient of inivtation
            $("#div_id_dinnerchoice_set-0-dinner_choice").addClass("hidden");

            // Guest 1
            $("#div_id_dinnerchoice_set-1-name").addClass("hidden");
            $("#div_id_dinnerchoice_set-1-dinner_choice").addClass("hidden");

            // Guest 2
            $("#div_id_dinnerchoice_set-2-name").addClass("hidden");
            $("#div_id_dinnerchoice_set-2-dinner_choice").addClass("hidden");

            // Guest 3
            $("#div_id_dinnerchoice_set-3-name").addClass("hidden");
            $("#div_id_dinnerchoice_set-3-dinner_choice").addClass("hidden");
        }
        
        hideEverything();
        
        /**************************************************
         * Handles clicking of attending or not
         *************************************************/
            // When "yes" is clicked, show Add Guest button
            $("#id_dinner_dancing_1").parents("li").click(function(){
                $("#addGuest").removeClass("hidden");
                $("#div_id_dinnerchoice_set-0-dinner_choice").removeClass("hidden");
                $("#dinner_descriptions").removeClass("hidden");
            });
        
            // When "no" is clicked, hide Add Guest button
            $("#id_dinner_dancing_0").parents("li").click(function(){
                hideEverything();
                $("#addGuest").addClass("hidden");
                $("#removeGuest").addClass("hidden");
                $("#div_id_dinnerchoice_set-0-dinner_choice").addClass("hidden");
                $("#dinner_descriptions").addClass("hidden");
            });
        
        /**************************************************
         * Adding or removing additional guests
         *************************************************/
            // Click to add guest
            $("#addGuest").click(function(){
                additionalGuests++;
                if(additionalGuests <= 3){
                    $("#div_id_dinnerchoice_set-" + additionalGuests + "-name").removeClass("hidden");
                    $("#div_id_dinnerchoice_set-" + additionalGuests + "-dinner_choice").removeClass("hidden");
                    $("#removeGuest").removeClass("hidden");
                    $("[name=dinnerchoice_set-TOTAL_FORMS]").val(additionalGuests+1);
                }
                
                if(additionalGuests == 3) {
                    $("#addGuest").addClass("hidden");
                }
            });
        
            // Click to remove guest
            $("#removeGuest").click(function(){
                $("#div_id_dinnerchoice_set-" + additionalGuests + "-name").addClass("hidden");
                $("#div_id_dinnerchoice_set-" + additionalGuests + "-dinner_choice").addClass("hidden");
                additionalGuests--;
                $("[name=dinnerchoice_set-TOTAL_FORMS]").val(additionalGuests+1);
                $("#addGuest").removeClass("hidden");
                if(additionalGuests == 0){
                    $("#removeGuest").addClass("hidden");
                }
            });
        
    }
});