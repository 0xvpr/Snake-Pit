#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h> // O_WRONLY

#include <stdio.h>
#include <errno.h>

int main(void)
{
    int   pipe_fd;
    char* path = "/tmp/data";
    char  buffer[256] = "exported data from bot 1";

    mkfifo(path, 0666);
    if ((pipe_fd = open(path, O_WRONLY)) < 0)
    {
        perror("Open");
        return -1;
    }
    write(pipe_fd, buffer, sizeof(buffer));

    close(pipe_fd);
    return 0;
}