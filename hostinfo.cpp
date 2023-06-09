// includes
#include <unistd.h>
#include <iostream>

/**
 * @brief defined some values
 * 
 */

#define HOST_NAME_MAX 1024
#define LOGIN_NAME_MAX 1024

/**
 * @brief chars, int
 * 
 */

char hostname[HOST_NAME_MAX];
char username[LOGIN_NAME_MAX];
int result;

/**
 * @brief main function
 * 
 * @return int 
 */

int main() 
{
    gethostname(hostname, HOST_NAME_MAX);
    getlogin_r(username, LOGIN_NAME_MAX);
    result = printf("Username: %s \nHostname: %s.\n",username, hostname);
    return 0;
}