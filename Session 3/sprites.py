from parts import *
'''
This class simply creates a part of a sprite and allows it to be placed on a sprite map.
'''

class sprite(object):
    def __init__(self,rows,cols): 
        self.row_count = cols
        self.col_count = rows
        self.pic =  np.array([[None for col in range(cols)] for row in range(rows)])
        self.x_loc = 0
        self.y_loc = 0
        self.part_map = 0
        self.name = ' '
        
    @property   
    def pos(self):
        return [self.x_loc,self.y_loc]
    
    @pos.setter
    def set_pos(self,value):
        self.x_loc = value[0]
        self.y_loc = value[1]
        
    @property
    def full_sprite(self):
        return self.pic
        
    @full_sprite.setter
    def set_sprite(self, value):
        '''
        Allow storing into class
        
        '''
        self.pic = value

    @full_sprite.deleter
    def del_sprite(self):
        print ("Instance Terminated")
        del self.pic   
    
    @property
    def sprite_name(self):
        return self.name
        
    @sprite_name.setter
    def set_name(self, value):
        self.name = value
        
    @sprite_name.deleter
    def del_name(self):
        del self.name
         
    def add_part(self,part,loc):
        self.pic = part.place_on_frame(self.pic,loc)
    
    def place_on_frame(self,frame_name,loc):
        self.x_loc = loc[1]
        self.y_loc = loc[0]
        for i in range(0,self.col_count):
                if i <= frame_name.shape[0]:
                    for j in range(self.row_count):
                        if j <= frame_name.shape[1]:
                            if self.pic[i][j] != None:
                                frame_name[loc[0]+i][loc[1]+j] = self.pic[i][j]
        return frame_name
        
    def view_sprite(self):
        #change None to 1's and display
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.pic[i][j] == None:
                    self.pic[i][j] = "FF"
        im_show(self.pic)