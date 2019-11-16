/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yoyassin <yoyassin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/25 00:00:25 by sid-bell          #+#    #+#             */
/*   Updated: 2019/11/16 15:35:21 by yoyassin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main(int x, char **a)
{
    int i = 0;

    // mode_t mode = 07777;
    // //while (1)
    int fd = open("/tmp/file", O_CREAT);
    // OPEN("file", O_CREAT,S_IRWXU | S_IRWXG | S_IRWXO);
    while(i < x)
    {
        // sleep(2);
        dprintf(1, "i2 = %s\n", a[i]);
        dprintf(2, "errs = %s\n", a[i]);
        i++;
    }
}
