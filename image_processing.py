import cv2

class ImageProcessorImpl:
     
    def CvtColor(src,roi): 
        src_copy=src
        src_copy_roi=src_copy[roi[0]:roi[1], roi[2]:roi[3]]
        dst_gray_roi=cv2.cvtColor(src_copy_roi,cv2.COLOR_RGB2GRAY)
       # src_copy[roi[0]:roi[0]+dst_gray_roi.shape[0], roi[2]:roi[2]+dst_gray_roi.shape[1]]=dst_gray_roi
        cv2.imshow(" ", dst_gray_roi)
        cv2.waitKey(0)
        return src_copy
   
    def Filter(src,roi,size):
        src_copy
        src_copy_roi=src_copy[roi[0]:roi[1], roi[2]:roi[3]]
        src_copy_roi=cv2.medianBlur(src_copy_roi,size) 
        cv2.imshow(" ", src_copy_roi)
        cv2.waitKey(0)
        return src_copy_roi
    
    def DetectEdges(src,roi,filter_size,low_threshold,ratio,kernel_size):
        src_copy=src
        src_copy_roi=src_copy[roi[0]:roi[1], roi[2]:roi[3]]
        src_gray_roi=cv2.cvtColor(src_copy_roi,cv2.COLOR_RGB2GRAY)
        gray_blurred=cv2.medianBlur(src_gray_roi,filter_size) 
        detected_edges=cv2.Canny(gray_blurred,low_threshold,ratio,kernel_size)
        cv2.imshow(" ", detected_edges)
        cv2.waitKey(0)
        dst=src
        return dst
    
    def Pixelize(src,roi,divs):
        src_copy=src
        src_copy_roi=src_copy[roi[0]:roi[1], roi[2]:roi[3]]
        block_size_x=(roi[1]-roi[0])/divs
        block_size_y=(roi[3]-roi[2])/divs
                
        
    
src_copy=cv2.imread('opencv_color.jpg')
src_copy_roi=[0,src_copy.shape[0],0,src_copy.shape[1]]
scr1=ImageProcessorImpl.CvtColor(src_copy,src_copy_roi)
scr2=ImageProcessorImpl.Filter(src_copy,src_copy_roi,7)
scr3=ImageProcessorImpl.DetectEdges(src_copy,src_copy_roi,15,15,15,15)
