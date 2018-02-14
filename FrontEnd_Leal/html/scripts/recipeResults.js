    window.onload = function(){
        document.querySelector('.cont_modal').className = "cont_modal";    
    }
    var c = 0;
    
function open_close(){
    if(c % 2 == 0){    
        this.document.querySelector('.cont_modal').className = "cont_modal cont_modal_active";
        c++;
    }else {
        this.document.querySelector('.cont_modal').className = "cont_modal";  
        c++;   
    } 
    
    
} 

function setRecipeImage(newSrc){
    document.getElementById("recipeImage").src = newSrc;
}

function addToFavorites(){
    /*add to favorites*/
    alert("Added to Favorites.");
    document.getElementById("bookmarkButton").innerHTML = "bookmark";
}

function load() {
    /*doesnt work yet*/
    var hi = "hello!" 
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    alert(hi);
    var fh = fso.OpenTextFile("/data/recipes/HawaiianBurger/recipeInstructions.txt", 1);
    var someOutput = fh.ReadAll();
    fso.close();
    document.getElementById("recipeInstructions").innerHTML = hi;
}

function openTab(tabName, barName) {
    var i;
    var x = document.getElementsByClassName("cont_text_det_preparation");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";
    }
    var x = document.getElementsByClassName("highBar");
    for (i = 0; i < x.length; i++) {
       x[i].style.borderTop = "7px solid rgba(237, 52, 108, 0)"; 
    
    }
    
    document.getElementById(tabName).style.display = "block";
    document.getElementById(barName).style.borderTop = "7px solid #ed346c";
    
}
    
    
    

    