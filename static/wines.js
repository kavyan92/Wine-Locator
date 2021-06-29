// when user clicks on save wine button, save that wine to user profile (my_wines.html)

$('#save-wine').on('click', (evt) => {
    evt.preventDefault();
    // set variable button for when clicked
    const button = $(evt.target);
    console.log("Form is here");
    // set variable buttonID
    const buttonId = button.attr('save-wine');
    
    // set variable to value of wine id on button form
    const formInput = {
      wineID: $('#wine-id').val(),
    };

    $.post('/my-wines', formInput, (res) => {
    // what we get back is res
    $('#my-wines').append(`<li>${wine.name}</li>`)
    })
  });