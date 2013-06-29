;(function($){
var site = window.site = new function() 
{
    this.init = function() 
    {
        //
    };


    this.ajax_call = function() 
    {
        var self = this;

        $('.button').bind('click', function(e) 
        {
            e.preventDefault();

            var slug = $(this).attr('id');

            Dajaxice.orzubalsky.ajax_load(
                self.ajax_load_callback, 
                {
                    'slug' : slug
                }
            );
        });	
    };


    this.ajax_load_callback = function(data)
    {
        $('#loader').hide();
        $('#dynamic').html(data);
    };
};
})(jQuery);

$(document).ready(function()
{
	site.init();
});		