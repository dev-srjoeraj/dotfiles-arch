
#!/bin/sh
case $BLOCK_BUTTON in
	1) setsid -f termite -e "tty-clock -s -b -t -B -c -C 3" ;;
esac

date "+ %I:%M%p"