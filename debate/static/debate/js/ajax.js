/**
 * Created by Steven on 8/31/17.
 */
$(function () {
   $('#search').keyup(function(){
       $.ajax({
           type: "POST",
           url: "/debate/search/",
           data: {
               'search_text': $('#search').val(),
               'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
           },
           success: searchSuccess,
           dataType: 'html'
       });
   });
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
}