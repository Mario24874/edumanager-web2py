# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------


# ---- example index page ----
def index():
    response.title = "EduManager"
 
    # Define the navigation menu
    menu_items = [
        ('Home', URL('default', 'index')),
        ('Students', URL('default', 'students')),
        ('Classrooms', URL('default', 'classrooms')),
        ('Subjects', URL('default', 'subjects')),
        ('Search', URL('default', 'search')),
        ('LOGIN', URL('default', 'user'))
    ]
    
    # Check if the user is logged in to display the LOGOUT link
    if auth.user:
        menu_items.append(('LOGOUT', URL('default', 'user', args=['logout'])))
    
    return dict(menu_items=menu_items)

    # ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin group
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

# ---- Additional routes for students, subjects, and classrooms ----
def students():
    """
    This function handles the view for the students page.
    """
    return dict()

def subjects():
    """
    This function handles the view for the subjects page.
    """
    return dict()

def classrooms():
    """
    This function handles the view for the classrooms page.
    """
    return dict()

from gluon.sqlhtml import SQLFORM

def classrooms():
    grid = SQLFORM.grid(db.classrooms, orderby=db.classrooms.name)
    return dict(grid=grid)

def subjects():
    grid = SQLFORM.grid(db.subjects, orderby=db.subjects.name)
    return dict(grid=grid)

