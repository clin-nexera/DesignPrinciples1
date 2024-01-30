# QUESTION: Where is SRP being violated?

class Camera():

    def connect(self, ip, port):
        # connect camera
        pass

        
    def check_valid_ip_and_port(self, ip, port): 
        # check valid ip and port format
        pass


    def disconnect(self):
        # disconnect camera
        pass


    def capture(self):
        # capture image
        pass

    
    def save_image(self, img, path): #??
        # save image to path
        pass


    def overlay_pcd_and_rgb(self, pcd, rgb): 
        # overlay pcd and rgb
        pass


    def convert_rgb_to_bgr(self, bgr): 
        # convert rgb to bgr
        pass




### Notes (There are no right answers) ###
    # check_valid_ip_and_port is doing two things
    # overlay_pcd_and_rgb and convert_rgb_to_bgr are more suitable under another class / file as they pertain more to image processing
    # save_image could also be in another class / file