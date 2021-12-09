import imghdr

print(imghdr.what('./result_data/image_temp_folder/305.jpg'))
if imghdr.what('./result_data/image_temp_folder/305.jpg') == 'jpeg':
    print('OK')

