#!/usr/bin/env bash

set -euo pipefail

REMOTE_USER="root"
REMOTE_IP="192.168.15.144"
REMOTE_DIR="/root/provision"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SSH="ssh ${REMOTE_USER}@${REMOTE_IP}"

sync_files() {
    echo "Syncing project..."
    rsync -avz \
        --delete \
        --exclude 'virt/' \
        --exclude '.git/' \
        --exclude '__pycache__/' \
        --exclude '*.pyc' \
        --exclude '*.sh' \
        -e ssh \
        "$SCRIPT_DIR/" \
        "${REMOTE_USER}@${REMOTE_IP}:${REMOTE_DIR}"
    echo "Sync completed."
}

stop_flask() {
    echo "Stopping Flask..."
    $SSH "killall flask || true"
}

start_flask() {
    $SSH "killall flask || true"
    echo "Starting Flask..."
    $SSH "cd ${REMOTE_DIR} && nohup flask --app hello run --host 100.64.0.1 --port 80 > flask.log 2>&1 &"
}

restart_flask() {
    stop_flask
    start_flask
}

show_logs() {
    $SSH "tail -f ${REMOTE_DIR}/flask.log"
}

usage() {
    echo "Usage: $0 {sync|start|stop|restart|logs|deploy}"
    exit 1
}

case "${1:-}" in
    sync)
        sync_files
        ;;
    start)
        start_flask
        ;;
    stop)
        stop_flask
        ;;
    restart)
        restart_flask
        ;;
    logs)
        show_logs
        ;;
    deploy)
        sync_files
        restart_flask
        ;;
    *)
        usage
        ;;
esac
