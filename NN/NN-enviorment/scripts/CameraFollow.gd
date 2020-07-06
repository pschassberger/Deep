extends Camera


func _ready():
	
	
	set_physics_process(true)
	
	set_as_toplevel(true)
	
func _physics_process(delta):
	var target = get_parent().get_global_transform().origin
	
