$(document).ready(function() {
    $('.carousel').carousel({
        interval: 3000
    });
    $('.toast').toast({
        delay: 3000,
    });
    $('.toast').toast('show')
});

// Set values in the modal to updated category
function showValuesInModal(slug, name, id){
    document.getElementById('categoryId').value = id
    document.getElementById('id_slug').value = slug
    document.getElementById('id_name').value = name
    document.getElementById('deleteBtn').hidden= false;
    document.getElementById('updateBtn').hidden= false;
    document.getElementById('addBtn').hidden= true;
    $("#CategoryModal").modal("show");
}

// Clear values in the modal to add new category
function clearValuesInModal(){
    document.getElementById('categoryId').value = ""
    document.getElementById('id_slug').value = ""
    document.getElementById('id_name').value = ""
    document.getElementById('deleteBtn').hidden= true;
    document.getElementById('updateBtn').hidden= true;
    document.getElementById('addBtn').hidden= false;
    $("#CategoryModal").modal("show");
}

// Filter lessons table
function filterTableLessons() {
    var input, filter, table, tr, td, cell, i, j;
  input = document.getElementById("searchLesson");
  filter = input.value.toUpperCase();
  table = document.getElementById("tableLessons");
  tr = table.getElementsByTagName("tr");

  for (i = 1; i < tr.length; i++) {
    // Hide the row initially.
    tr[i].style.display = "none";
  
    td = tr[i].getElementsByTagName("td");
    for (var j = 0; j < td.length; j++) {
      cell = tr[i].getElementsByTagName("td")[j];
      if (cell) {
        if (cell.innerHTML.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          break;
        } 
      }
    }
  }
}




  