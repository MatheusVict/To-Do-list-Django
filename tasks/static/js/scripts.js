$(document).ready(function() {
    
    const baseUrl ='https://to-do-list-django-matheus.herokuapp.com/';
    const deletar = $('.delete-btn');
    const searchBtn = $('#search-btn');
    const searchForm = $('#search-form');
    const filter = $('#filter');

    $(deletar).on('click', function(e) {

        e.preventDefault();

        const dletlink = $(this).attr('href');
        const result = Swal.fire({
            title: 'Deseja apagar essa tarefa?',
            showDenyButton: true,
            confirmButtonText: 'Sim',
            denyButtonText: `Não`,
          }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
              Swal.fire('Apagada!', '', 'success')
              window.location.href = dletlink;
            } else if (result.isDenied) {
              Swal.fire('A tarefa não foi apagada', '', 'info')
            }
          });

    });

  $(searchBtn).on('click', function() { // Função q faz a lupa fazer o submit do formulario get(A busca)
    searchForm.submit();
  });

  $(filter).change(function() {
    const filter = $(this).val();
    window.location.href = baseUrl + '?filter=' + filter;
  });


});
