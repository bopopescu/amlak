$(document).ready(function(){
    load_json_data('id_ostan');
    function load_json_data(id,parent_id)
    {
        var html_code='';
        
        $.getJSON('/static/json/province.json', function(data){
            html_code += '<option value="">گزینه مورد نظر را انتخاب کنید</option>';  
            $.each(data, function(key, value){
              
                if(id =='id_ostan')
                {
                    
                    if(value.parent_id=='998')
                    {
                        
                      html_code += '<option value="'+value.id+'">'+value.title+'</option>'; 
                    }
                }
                else 
                {
                    
                    if(value.parent_id== parent_id)
                    {
                       
                        html_code += '<option value="'+value.id+'">'+value.title+'</option>';
                    }
                }
              
            });
            
            $('#'+id).html(html_code);
            id= ('#'+id).value.id;
            alert(id);
            
            
        });
    }
    $(document).on('change','#id_ostan', function(){
        var ostan_id = $(this).val();
        if(ostan_id !='')
        {
           load_json_data('id_city',ostan_id);
           
        }
        else
        {
            $('#id_ostan').html('<option value=""> استان</option>');
            $('#id_city').html('<option value=""> شهرستان</option>');
            
          
        }
    
    });

    // $(document).on('change','#ostan', function(){
    //     var ostan_id = $(this).val();
    //     if(ostan_id != '')
    //     {
    //         load_json_data('city', ostan_id);

    //     }
    //     else
    //     {
    //         $('#city').html('<option value="">Select City</option>');
    //         // {% comment %} $('#state').html('<option value="">Select State</option>'); {% endcomment %}
    //     }
        
        
    // });

    // $(document).on('change','#city', function(){
    //     var city_id = $(this).val();
    //     if(city_id != '')
    //     {
    //         load_json_data('city', city_id);

    //     }
    //     else
    //     {
    //         $('#city').html('<option value="">Select City</option>');
    //     }
        
        
    // });

    
});