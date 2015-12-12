/*
http://stackoverflow.com/questions/11519759/how-to-read-low-level-mouse-click-position-in-linux
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <linux/input.h>
#include <fcntl.h>

//select input here
#define MOUSEFILE "/dev/input/by-id/usb-MCNEX_SC-20FHL11149M-event-if00"

int main()
{
    int fd;
    struct input_event ie;

    if((fd = open(MOUSEFILE, O_RDONLY)) == -1) {
        perror("opening device");
        exit(EXIT_FAILURE);
    }

    while(read(fd, &ie, sizeof(struct input_event))) {
        printf("type %d\tcode %d\tvalue %d\n",
               ie.type, ie.code, ie.value);

}
    return 0;
}
