from django import template

register = template.Library()

@register.filter(name='get_resource_type')
def get_resource_type(pending, index):
    index = int(index)
    print(pending[index])
    return pending[index].resource_id.resource_type

@register.filter(name='get_resource_id')
def get_resource_id(pending, index):
    index = int(index)
    print(pending[index])
    return pending[index].resource_id.resource_id

@register.filter(name='get_topic_id')
def get_topic_id(pending, index):
    index = int(index)
    print(pending[index])
    return pending[index].topic_id.topic_id

@register.filter(name='get_subtopic_id')
def get_subtopic_id(pending, index):
    index = int(index)
    print(pending[index])
    return pending[index].resource_id.subtopic_id            

@register.filter(name='sub')
def sub(val, args):
    return str(int(val) - int(args))

@register.filter(name='integer')
def integer(val):
	return int(val)    

@register.filter(name='get_status')
def get_status(pending,index):
	index = int(index)
	return pending[index].status	

@register.filter(name="get_resource_link") 
def get_resource_link(pending,index):
    index = int(index)
    return pending[index].resource_id.resource_link